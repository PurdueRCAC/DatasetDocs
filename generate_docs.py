#!/usr/bin/env python3
"""
generate_docs.py

Recursively scans a directory of Lmod (.lua) files for datasets
(e.g., /opt/spack/datasets).
For each .lua file:
  1. Parses the multi-line help text.
  2. Extracts environment variables (setenv).
  3. Writes out an .rst file mirroring the directory structure.

Enhancements:
  - Parse the date from .lua filename as "version" if it matches YYYY-MM-DD.
  - Generate an index.rst per top-level category folder referencing all dataset .rst files.
  - Generate a main docs/index.rst that references each category's index.rst.
  - Style environment variables in a more detailed table.

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

# Regex patterns
HELP_PATTERN = re.compile(r'help\s*\(\[\[\s*(.*?)\s*\]\]\)', flags=re.DOTALL)
# Allow the second argument to be:
#   - a quoted string (possibly with internal . or / ), OR
#   - an unquoted expression until the next closing paren
SETENV_PATTERN = re.compile(
    r'setenv\s*\(\s*"([^"]+)"\s*,\s*(.*?)\)\s*'
    # Explanation:
    # 1) setenv(
    # 2) "([^"]+)"    -> capture the env var name inside quotes
    # 3) ,\s*        -> comma and some optional whitespace
    # 4) (.*?)\)     -> capture everything (non-greedy) until the first closing parenthesis
    # 5) optional spaces after ) are also allowed
    , flags=re.DOTALL
)
DATE_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2})')  # captures YYYY-MM-DD

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
    content = lua_file.read_text(encoding="utf-8")

    # 1. Grab the help text
    help_match = HELP_PATTERN.search(content)
    help_text = help_match.group(1) if help_match else ""

    # 2. Find all setenv lines
    envvars = {}
    for match in SETENV_PATTERN.finditer(content):
        env_var = match.group(1).strip()      # first capture: variable name
        val_raw = match.group(2).strip()      # second capture: everything up to ')'

        # If the value is wrapped in quotes, remove them
        # e.g. "some/path" or "modroot.."/etc"
        if val_raw.startswith('"') and val_raw.endswith('"'):
            val_raw = val_raw[1:-1]

        # Now store it in the dictionary
        envvars[env_var] = val_raw

    return help_text, envvars
      

def extract_version_from_filename(filename: str):
    """
    Attempt to extract a date (YYYY-MM-DD) as the version
    from a .lua filename, e.g. '2022-10-17.lua' => '2022-10-17'.
    If no date-like pattern is found, return the filename minus extension.
    """
    base = filename.replace('.lua', '')
    # Look for the first YYYY-MM-DD pattern
    match = DATE_PATTERN.search(base)
    if match:
        return match.group(1)  # e.g. 2022-10-17
    else:
        # fallback
        return base

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

    Example structure in the RST:

        =====================================
        Dataset: {dataset_name} ({version})
        =====================================

        Category: {category}

        {help_text}

        **Environment Variables**

        +------------------------+-------------------------------------------+
        | Variable Name          | Value                                     |
        +========================+===========================================+
        | ERA5_ERA5GRIB         | /anvil/datasets/ERA5/ERA5GRIB             |
        +------------------------+-------------------------------------------+
        | ERA5_HOME             | /anvil/datasets/ERA5                      |
        +------------------------+-------------------------------------------+

    """
    title_line = f"Dataset: {dataset_name} ({version})"
    underline = "=" * len(title_line)

    # Create an RST table for environment variables
    # We'll use the "grid" table style for clarity
    env_table_lines = []
    if envvars:
        env_table_lines.append("**Environment Variables**\n")
        col_width_var = max(len(k) for k in envvars.keys()) + 2
        col_width_val = max(len(v) for v in envvars.values()) + 2
        # Create table header
        header = (
            "+" + "-" * col_width_var + "+" + "-" * col_width_val + "+\n"
            "| Variable Name" + " " * (col_width_var - len(" Variable Name")) +
            "| Value" + " " * (col_width_val - len(" Value")) + "|\n"
            "+" + "=" * col_width_var + "+" + "=" * col_width_val + "+\n"
        )
        env_table_lines.append(header)

        # Fill table rows
        for name, val in envvars.items():
            row = (
                f"| {name}" + " " * (col_width_var - len(name) - 1) +
                f"| {val}" + " " * (col_width_val - len(val) - 1) + "|\n"
                "+" + "-" * col_width_var + "+" + "-" * col_width_val + "+\n"
            )
            env_table_lines.append(row)
    else:
        # If no env vars, still note that
        env_table_lines.append("\n(No environment variables found)\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{underline}\n{title_line}\n{underline}\n\n")
        f.write(f"Category: **{category}**\n\n")
        f.write(help_text.strip() + "\n\n")
        f.write("".join(env_table_lines))
        f.write("\n")

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
    #   category -> {
    #       subdir_key -> list of (version, dataset_rst_path, dataset_name)
    #   }
    # where subdir_key is the path *after* category. For example:
    #   Covariates/AboveBelowRatio => subdir_key="AboveBelowRatio"
    #   If there's no deeper subdir, it might just be "" or the same as category
    categories_dict = defaultdict(lambda: defaultdict(list))

    for root, dirs, files in os.walk(datasets_dir):
        root_path = Path(root)

        # Identify .lua files
        lua_files = [f for f in files if f.endswith('.lua')]
        if not lua_files:
            continue

        # Relative path from datasets_dir (e.g. Covariates/AboveBelowRatio)
        rel_path = root_path.relative_to(datasets_dir)
        parts = rel_path.parts
        if len(parts) == 0:
            # means root == datasets_dir
            continue

        category = parts[0]
        # The remainder is the subdir_key (which can be multiple levels)
        subdir_key = "/".join(parts[1:]) if len(parts) > 1 else ""

        # Process each .lua file
        for lua_file in lua_files:
            lua_path = root_path / lua_file
            help_text, envvars = parse_lua_file(lua_path)
            version = extract_version_from_filename(lua_file)

            # The "dataset_name" might be the subdir_key if it exists,
            # or the category if no subdir_key.
            # But in some HPC setups, the single subdir can be the actual dataset.
            # We'll just treat subdir_key as the "dataset name" if it’s non-empty.
            # If it has multiple levels, we'll keep them joined by '/'.
            dataset_name = subdir_key if subdir_key else category

            # Construct an output directory that mirrors the structure
            # i.e. docs/Covariates/AboveBelowRatio
            output_subdir = output_dir / category / subdir_key
            output_subdir.mkdir(parents=True, exist_ok=True)

            # We'll name our .rst file e.g. 2022-10-17.rst
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

            # Record it for index creation
            categories_dict[category][subdir_key].append(
                (version, output_file, dataset_name)
            )

    # -------------------------------------------------------------------
    # (3) Generate an index.rst for each top-level category
    # -------------------------------------------------------------------
    for category, subdict in categories_dict.items():
        category_path = output_dir / category
        index_file = category_path / "index.rst"
        # We'll overwrite it with a fresh index
        with open(index_file, 'w', encoding='utf-8') as f_idx:
            title = f"{category} Datasets"
            underline = "=" * len(title)
            f_idx.write(f"{underline}\n{title}\n{underline}\n\n")
            f_idx.write(".. toctree::\n")
            f_idx.write("   :maxdepth: 2\n")
            f_idx.write("   :caption: Sub-Datasets\n\n")

            # For each subdir_key (e.g. AboveBelowRatio), create an entry
            # If subdir_key is empty, it means the .lua was directly under category
            for subdir_key, items in sorted(subdict.items()):
                # If subdir_key is "" => same folder; else subdirKey is the subfolder
                if subdir_key:
                    # We can create a subdir index or just list each .rst
                    # But let's do a subdir index if more than one .rst is present.
                    subdir_path = category_path / subdir_key
                    subdir_index = subdir_path / "index.rst"
                    # Generate a subdir-level index
                    with open(subdir_index, 'w', encoding='utf-8') as sf:
                        sub_title = f"{subdir_key} Datasets"
                        sub_underline = "=" * len(sub_title)
                        sf.write(f"{sub_underline}\n{sub_title}\n{sub_underline}\n\n")
                        sf.write(".. toctree::\n")
                        sf.write("   :maxdepth: 2\n")
                        sf.write("   :caption: Versions\n\n")

                        # Sort by version for consistent ordering
                        sorted_items = sorted(items, key=lambda x: x[0])
                        for (version, rst_path, dataset_name) in sorted_items:
                            # Compute relative path from subdir_index to the .rst
                            # We'll just use the filename since they're in the same folder
                            rst_file = rst_path.name
                            sf.write(f"   {rst_file}\n")

                    # Now reference the subdir index from the category index:
                    rel_subdir_index = f"{subdir_key}/index"
                    f_idx.write(f"   {rel_subdir_index}\n")
                else:
                    # Subdir key is empty => RSTs are directly under the category folder
                    # We just list them here
                    sorted_items = sorted(items, key=lambda x: x[0])
                    for (version, rst_path, dataset_name) in sorted_items:
                        rst_file = rst_path.name
                        f_idx.write(f"   {rst_file}\n")

            f_idx.write("\n")

    # -------------------------------------------------------------------
    # (1) Automatically update the main docs/index.rst
    # -------------------------------------------------------------------
    main_index = output_dir / "index.rst"
    with open(main_index, 'w', encoding='utf-8') as f_main:
        main_title = "Federated Datasets Documentation"
        main_underline = "=" * len(main_title)
        f_main.write(f"{main_underline}\n{main_title}\n{main_underline}\n\n")
        f_main.write("Welcome! Below are the top-level dataset categories.\n\n")
        f_main.write(".. toctree::\n")
        f_main.write("   :maxdepth: 2\n")
        f_main.write("   :caption: Categories\n\n")

        # Reference each category’s index.rst
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

