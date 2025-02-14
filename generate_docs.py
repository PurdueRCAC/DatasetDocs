#!/usr/bin/env python3
"""
generate_docs.py

Recursively scans a directory of Lmod (.lua) files for datasets
(e.g., /opt/spack/datasets). For each .lua file:
  1. Parses the multi-line help text.
  2. Extracts environment variables (setenv).
  3. Writes out an .rst file mirroring the directory structure.

Enhancements:
  - Parse the date from .lua filename as "version" if it matches YYYY-MM-DD.
  - Generate an index.rst per top-level category, but NOT per subdirectory.
  - Use a reST list-table for environment variables (nicely rendered in RTD).

Usage:
  python generate_docs.py \
    --datasets-dir /opt/spack/datasets \
    --output-dir /path/to/DatasetDocs/docs
"""

import os
import re
import argparse
from pathlib import Path
from collections import defaultdict

HELP_PATTERN = re.compile(
    r'help\s*\(\[\[\s*(.*?)\s*\]\]\)',
    flags=re.DOTALL
)

# Flexible pattern to handle various setenv() argument styles
SETENV_PATTERN = re.compile(
    r'setenv\s*\(\s*"([^"]+)"\s*,\s*(.*?)\)\s*',
    flags=re.DOTALL
)

# Looks for a YYYY-MM-DD pattern in the filename
DATE_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2})')

def parse_lua_file(lua_file: Path):
    """
    Parse a single Lua file to extract:
      1. The multi-line help text from help([[...]])
      2. setenv(...) environment variables
    Returns:
      (help_text, envvars)
        help_text = str containing everything in help([[]])
        envvars   = dict of {ENV_VAR_NAME: raw_value}
    """
    content = lua_file.read_text(encoding='utf-8')

    # First find modroot if it exists
    modroot_pattern = re.compile(r'local\s+modroot\s*=\s*"([^"]+)"')
    modroot_match = modroot_pattern.search(content)
    modroot = modroot_match.group(1) if modroot_match else ""

    # Extract help text (first match)
    help_match = HELP_PATTERN.search(content)
    help_text = help_match.group(1) if help_match else ""

    # Extract environment variables
    envvars = {}
    for match in SETENV_PATTERN.finditer(content):
        env_var = match.group(1).strip()
        val_raw = match.group(2).strip()

        # Remove wrapping quotes if present
        if val_raw.startswith('"') and val_raw.endswith('"'):
            val_raw = val_raw[1:-1]
        
        # Handle modroot concatenation (modroot.."/path" or just modroot)
        if 'modroot' in val_raw:
            if val_raw == 'modroot':
                val_raw = modroot
            else:
                # Replace modroot.."/path" with actual path
                val_raw = val_raw.replace('modroot..', '')
                if val_raw.startswith('"'):
                    val_raw = val_raw[1:]
                if val_raw.endswith('"'):
                    val_raw = val_raw[:-1]
                val_raw = modroot + val_raw

        envvars[env_var] = val_raw

    return help_text, envvars

def extract_version_from_filename(filename: str):
    """
    Attempt to extract a date (YYYY-MM-DD) as the version
    from a .lua filename, e.g. '2022-10-17.lua' => '2022-10-17'.
    If no date-like pattern is found, return the filename minus extension.
    """
    base = filename.replace('.lua', '')
    match = DATE_PATTERN.search(base)
    if match:
        return match.group(1)  # e.g. 2022-10-17
    else:
        return base

def clean_help_text(help_text: str) -> str:
    """
    Remove only the environment variables listing section from help text if present.
    Removes everything from 'Environment variables included:' through the variable listings,
    up to but not including the Tips section or next major section.
    Also cleans up line wrapping and formatting.
    """
    # Pattern to match the environment variables section:
    # Starts with "Environment variables included:"
    # Followed by dashed line
    # Contains variable listings
    # Ends at the last environment variable or "additional variables not shown" line
    # Stops before Tips or next section
    env_section_pattern = re.compile(
        r'Environment variables included:\s*\n-{5,}\n(?:.*?\$[^\n]+\n)+(?:.*?additional.*?not shown.*?\n\n)?(?:\$[^\n]+\n)*\n',
        re.DOTALL | re.MULTILINE
    )
    
    # Remove just the environment variables listing section
    cleaned_text = env_section_pattern.sub('\n', help_text)
    
    # Split into lines and process
    lines = cleaned_text.split('\n')
    fixed_lines = []
    current_paragraph = []
    in_list = False
    in_tips = False
    in_attributes = False
    
    for line in lines:
        stripped = line.strip()
        
        # Handle empty lines - they mark paragraph boundaries
        if not stripped:
            if current_paragraph:
                fixed_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            fixed_lines.append('')
            continue
            
        # Handle Tips section
        if stripped == 'Tips:':
            if current_paragraph:
                fixed_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            fixed_lines.append('**Tips:**\n')  # Make it bold in RST and add newline
            in_tips = True
            in_attributes = False
            continue
            
        # Handle attributes section
        if stripped == 'This dataset contains data with the following attributes:':
            if current_paragraph:
                fixed_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            fixed_lines.append(stripped + '\n')  # Add extra newline for list
            in_attributes = True
            in_tips = False
            continue
            
        # Handle list items
        if stripped.startswith('- '):
            if current_paragraph:
                fixed_lines.append(' '.join(current_paragraph))
                current_paragraph = []
            # Format as proper RST bullet list with proper indentation
            if in_tips or in_attributes:
                fixed_lines.append('* ' + stripped[2:])
                fixed_lines.append('')  # Add blank line after each bullet point
            else:
                fixed_lines.append(stripped)
            in_list = True
            continue
            
        # Handle dashed lines - skip them
        if re.match(r'^-+$', stripped):
            continue
            
        # Regular paragraph text
        if in_list:
            fixed_lines.append(stripped)
        else:
            current_paragraph.append(stripped)
    
    # Don't forget the last paragraph
    if current_paragraph:
        fixed_lines.append(' '.join(current_paragraph))
    
    # Join lines and clean up
    cleaned_text = '\n'.join(fixed_lines)
    
    # Clean up multiple newlines but preserve intentional spacing
    cleaned_text = re.sub(r'\n{3,}', '\n\n', cleaned_text)
    cleaned_text = re.sub(r' +', ' ', cleaned_text)  # Normalize spaces within lines
    
    return cleaned_text.strip()

def generate_rst_file(
    category: str,
    dataset_name: str,
    version: str,
    help_text: str,
    envvars: dict,
    output_file: Path
):
    """
    Write an .rst file capturing the help text and environment variables.

    Structure:
        =====================================
        {dataset_name}
        =====================================

        Category: {category}

        Description
        -----------
        {help_text}

        Usage
        -----
        To find and load available datasets::

            $ module avail
            $ module load datasets
            $ module spider datasets/{category}/{dataset_name}

        Environment Variables
        -------------------
        {env_table}
    """
    title_line = dataset_name  # Simplified title
    underline = "=" * len(title_line)

    # Clean the help text to remove environment variables section
    cleaned_help_text = clean_help_text(help_text)

    # Create a list-table for environment variables
    if envvars:
        env_table_lines = []
        env_table_lines.append(".. list-table::")
        env_table_lines.append("   :header-rows: 1")
        env_table_lines.append("   :widths: 25 75")
        env_table_lines.append("")
        env_table_lines.append("   * - **Variable Name**")
        env_table_lines.append("     - **Value**")

        for name, val in envvars.items():
            env_table_lines.append(f"   * - ``{name}``")
            env_table_lines.append(f"     - ``{val}``")

        env_table = "\n".join(env_table_lines)
    else:
        # If no env vars
        env_table = "(No environment variables found)\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        # Title
        f.write(f"{underline}\n{title_line}\n{underline}\n\n")
        
        # Version (as a subtitle)
        if version:
            f.write(f"Version: {version}\n\n")
        
        # Category
        f.write(f"Category: **{category}**\n\n")
        
        # Description section
        f.write("Description\n")
        f.write("-----------\n\n")
        f.write(cleaned_help_text + "\n\n")
        
        # Usage section
        f.write("Usage\n")
        f.write("-----\n\n")
        f.write("To find and load available datasets::\n\n")
        f.write("    $ module avail\n")
        f.write("    $ module load datasets\n")
        f.write(f"    $ module load {category}/{dataset_name}/{version}\n")
        
        # Environment Variables section
        f.write("Environment Variables\n")
        f.write("-------------------\n\n")
        f.write(env_table + "\n")

def main():
    parser = argparse.ArgumentParser(description="Generate .rst docs from Lmod .lua files.")
    parser.add_argument("--datasets-dir", required=True,
                        help="Top-level directory containing dataset folders (e.g. /opt/spack/datasets).")
    parser.add_argument("--output-dir", required=True,
                        help="Directory where .rst files should be saved (e.g. /path/to/DatasetDocs/docs).")

    args = parser.parse_args()
    datasets_dir = Path(args.datasets_dir).resolve()
    output_dir = Path(args.output_dir).resolve()

    # This dict will map:
    #   category -> list of (version, rst_path, dataset_name)
    #
    # We'll flatten subdirectories so that only each top-level category
    # has a single index.rst referencing all .rst files below it.
    categories_dict = defaultdict(list)

    # --- Walk the datasets directory ---
    for root, dirs, files in os.walk(datasets_dir):
        root_path = Path(root)

        # Identify .lua files
        lua_files = [f for f in files if f.endswith('.lua')]
        if not lua_files:
            continue

        # The relative path from the top-level datasets_dir
        rel_path = root_path.relative_to(datasets_dir)
        parts = rel_path.parts

        if len(parts) == 0:
            # means root == datasets_dir
            continue

        # The first part is the category
        category = parts[0]

        # The remainder is the subdirectory structure
        subdir_key = "/".join(parts[1:]) if len(parts) > 1 else ""

        for lua_file in lua_files:
            lua_path = root_path / lua_file
            help_text, envvars = parse_lua_file(lua_path)
            version = extract_version_from_filename(lua_file)

            # If there's a subdir_key, we treat that as "dataset_name" (plus any deeper path).
            # If none, it's just the category name. 
            # Example: 
            #   Covariates/AboveBelowRatio => dataset_name=AboveBelowRatio 
            #   (if there's more, we keep it joined by "/")
            dataset_name = subdir_key if subdir_key else category

            # Mirror the folder structure in output
            # i.e. docs/Covariates/AboveBelowRatio/2022-10-17.rst
            output_subdir = output_dir / category / subdir_key
            output_subdir.mkdir(parents=True, exist_ok=True)

            rst_filename = f"{version}.rst"
            output_file = output_subdir / rst_filename

            generate_rst_file(
                category=category,
                dataset_name=dataset_name,
                version=version,
                help_text=help_text,
                envvars=envvars,
                output_file=output_file
            )

            # We'll store it so we can add it to the category's toctree
            categories_dict[category].append(output_file)

    # --- Generate one index.rst for each top-level category ---
    for category, rst_files in categories_dict.items():
        category_path = output_dir / category
        index_file = category_path / "index.rst"

        # Sort the references for consistency
        # We can sort by relative path or by filename
        rst_files_sorted = sorted(rst_files)

        with open(index_file, 'w', encoding='utf-8') as f_idx:
            title = f"{category} Datasets"
            underline = "=" * len(title)
            f_idx.write(f"{underline}\n{title}\n{underline}\n\n")

            f_idx.write(".. toctree::\n")
            f_idx.write("   :maxdepth: 2\n")
            f_idx.write("   :caption: Datasets\n\n")

            for rst_file in rst_files_sorted:
                # Convert absolute path to relative path from the category folder
                rel_path = rst_file.relative_to(category_path)
                # Sphinx wants the path without the .rst extension in the toctree reference
                reference = rel_path.as_posix().replace(".rst", "")
                f_idx.write(f"   {reference}\n")

            f_idx.write("\n")

    # --- Automatically update the main docs/index.rst ---
    main_index = output_dir / "index.rst"
    with open(main_index, 'w', encoding='utf-8') as f_main:
        main_title = "Federated Datasets Documentation"
        main_underline = "=" * len(main_title)
        f_main.write(f"{main_underline}\n{main_title}\n{main_underline}\n\n")
        f_main.write("Welcome! Below are the top-level dataset categories.\n\n")

        f_main.write(".. toctree::\n")
        f_main.write("   :maxdepth: 2\n")
        f_main.write("   :caption: Categories\n\n")

        # Reference each category's index.rst
        for category in sorted(categories_dict.keys()):
            f_main.write(f"   {category}/index\n")

        f_main.write("\n")
        f_main.write("Indices and tables\n")
        f_main.write("==================\n\n")
        f_main.write("* :ref:`genindex`\n")
        f_main.write("* :ref:`modindex`\n")
        f_main.write("* :ref:`search`\n")
        f_main.write("\n")


if __name__ == "__main__":
    main()


