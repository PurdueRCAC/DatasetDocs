import textwrap
import json
import os
import re

from datetime import datetime

# base directories
input_base_dir = "/anvil/datasets"
output_base_dir = "Anvil-Modulefiles/datasets"

# constants for cutoffs
SUBDIR_CUTOFF = 25  # maximum number of subdirectories allowed per folder
METADATA_FILE_CUTOFF = 10  # maximum number of metadata files allowed per folder
SHOW_LIMIT = 5 # Number of environment variables to display
WRAP_WIDTH = 120  # define the title length for wrapping

# dataset metadata
#       Folder
#       Time resolution
#       Spatial Resolution
#       DOI
#       Link 
#       Publication Date
#       Title 
#       Description

## LOADED FROM JSON

def load_metadata(json_file):
    """
    Load dataset metadata from a JSON file.
    
    Args:
        json_file (str): Path to the JSON file containing metadata.
    
    Returns:
        dict: Parsed metadata.
    """
    try:
        with open(json_file, "r") as file:
            metadata = json.load(file)
            return metadata
    except FileNotFoundError:
        print(f"Error: Metadata file '{json_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON from '{json_file}'. Please check the file format.")
        exit(1)


def sanitize_env_var_name(name):
    """
    Sanitize the environment variable name to conform to allowed characters:
    - Only allow a-z, A-Z, 0-9, and underscores.
    - Replace invalid characters with underscores.
    - Ensure the name does not start with a number by prefixing it with an underscore if necessary.
    """
    sanitized_name = re.sub(r"[^a-zA-Z0-9_]", "_", name)  # Replace invalid characters with underscores
    if re.match(r"^\d", sanitized_name):  # Prefix with an underscore if it starts with a number
        sanitized_name = f"_{sanitized_name}"
    return sanitized_name



def analyze_directory(path, naming_convention):
    """
    Analyze the directory structure to extract key subdirectories and potential metadata files.
    - Skip children of directories exceeding SUBDIR_CUTOFF.
    - Skip metadata files if their count exceeds METADATA_FILE_CUTOFF.
    - Parent directories are always included as environment variables.
    """
    env_vars = {}
    metadata_file_extensions = {".txt", ".json", ".yaml", ".yml", ".sh"}  # Includes .sh for shell files

    for root, dirs, files in os.walk(path):
        relative_path = os.path.relpath(root, path).strip(".")
        
        # Skip processing if the relative path is the root (".")
        if relative_path == "":
            continue

        # Always include the parent directory unless it is the root directory (handled by HOME)
        if relative_path != ".":
            var_name = sanitize_env_var_name(f"{naming_convention}_{relative_path.replace('/', '_').upper()}")
            env_vars[var_name] = root

        # Check if the current directory's children exceed the subdirectory cutoff
        if len(dirs) > SUBDIR_CUTOFF:
            print(f"Skipping children of {relative_path} due to exceeding subdirectory count cutoff ({len(dirs)} > {SUBDIR_CUTOFF}).")
            dirs[:] = []  # Clear dirs to skip processing its children
            continue

        # Process subdirectories if below cutoff
        for subdir in sorted(dirs):  # Sort subdirectories alphabetically
            subdir_path = os.path.join(relative_path, subdir)
            var_name = sanitize_env_var_name(f"{naming_convention}_{subdir_path.replace('/', '_').upper()}")
            env_vars[var_name] = os.path.join(root, subdir)

        # Check if metadata files exceed the cutoff
        metadata_files = [file for file in files if os.path.splitext(file)[1].lower() in metadata_file_extensions]
        if len(metadata_files) > METADATA_FILE_CUTOFF:
            print(f"Skipping metadata files in {relative_path} due to exceeding file count cutoff ({len(metadata_files)} > {METADATA_FILE_CUTOFF}).")
            continue

        # Process metadata files (if below cutoff)
        for file in sorted(metadata_files):  # Sort metadata files alphabetically
            file_path = os.path.join(relative_path, file)
            var_name = sanitize_env_var_name(f"{naming_convention}_{file_path.replace('/', '_').upper()}")
            env_vars[var_name] = os.path.join(root, file)

    # Return sorted environment variables
    return dict(sorted(env_vars.items()))


def generate_module_file(output_dir, dataset_name, folder_name, modroot, metadata, env_vars):
    """
    Generate the module file with dynamic help section and environment variables.
    Automatically wraps the description to align with the title length.
    """
    os.makedirs(output_dir, exist_ok=True)
    # use publication date for versioning
    publication_date = datetime.strptime(metadata["publication_date"], "%Y-%m-%d").strftime("%Y-%m-%d")
    lua_file = os.path.join(output_dir, f"{publication_date}.lua")

    # compute maximum variable name length for proper alignment
    max_var_len = max(len(var) for var in env_vars.keys()) if env_vars else 0
    max_var_len = max(max_var_len, len(f"{dataset_name}_VERSION"))  # Ensure spacing works for VERSION line

    with open(lua_file, "w") as f:
        # header and help section
        f.write("help([[\n")
        f.write(f"{metadata['title']}\n")
        f.write("\n")
        wrapped_description = textwrap.fill(metadata['description'], width=WRAP_WIDTH)
        f.write(f"{wrapped_description}\n\n")
        f.write(f"This dataset contains data with the following attributes:\n")
        f.write(f"  - Time Resolution: {metadata.get('time_resolution', 'N/A')}\n")
        f.write(f"  - Spatial Resolution: {metadata.get('spatial_resolution', 'N/A')}\n")
        f.write(f"  - DOI: {metadata.get('doi', 'N/A')}\n")
        f.write(f"  - Link: {metadata.get('link', 'N/A')}\n\n")
        f.write("Environment variables included:\n")
        f.write("-------------------------------------------------------------\n")
        env_var_list = list(env_vars.items())                      # show only the first few variables up to SHOW_LIMIT
        for var, path in env_var_list[:SHOW_LIMIT]:
            f.write(f"${var:<{max_var_len}}  Location: {path}\n")
        remaining_count = len(env_var_list) - SHOW_LIMIT           # count and display the remaining variables
        if remaining_count > 0:
            f.write(f"\n{remaining_count} additional environment variables not shown.\n")
        f.write("\n")
        f.write(f"${dataset_name}_HOME{' ' * (max_var_len - len(dataset_name) - 3)}Location: {modroot}\n")
        f.write(f"${dataset_name}_ROOT{' ' * (max_var_len - len(dataset_name) - 3)}Location: {modroot}\n")
        f.write(f"${dataset_name}_VERSION{' ' * (max_var_len - len(dataset_name) - 6)}Version: {publication_date}\n")
        f.write("\n")
        f.write("Tips:\n")
        f.write(f"- Use echo $ENV_NAME to check the environment value.\n")
        f.write(f"- To see all environment variables related to {dataset_name}, you can load the module then use: env | grep {dataset_name}\n")
        f.write(f"- To unload the module and remove the environment settings: module unload {dataset_name}\n")
        f.write("-------------------------------------------------------------\n]])\n\n")

        # add module root path
        f.write(f'local modroot="{modroot}"\n\n')

        # add environment variables
        for var, path in env_vars.items():
            f.write(f'setenv("{var}", modroot.."/{os.path.relpath(path, modroot)}")\n')

        # add footer
        f.write(f'\nsetenv("{dataset_name}_HOME", modroot)\n')
        f.write(f'setenv("RCAC_{dataset_name}_ROOT", modroot)\n')
        f.write(f'setenv("RCAC_{dataset_name}_VERSION", "{publication_date}")\n')


def main():
    """
    Main script to generate the module files for all datasets.
    """
    # Load dataset metadata from a JSON file
    json_file = "covariates.json"  # Specify your JSON file here
    dataset_metadata = load_metadata(json_file)

    for category, datasets in dataset_metadata.items():
        for dataset_name, metadata in datasets.items():
            folder_name = metadata["folder"]
            input_dir = os.path.join(input_base_dir, category, folder_name)
            output_dir = os.path.join(output_base_dir, category, folder_name)

            if not os.path.exists(input_dir):
                print(f"Warning: Dataset folder {input_dir} does not exist. Skipping.")
                continue

            # Analyze and then generate module file
            env_vars = analyze_directory(input_dir, dataset_name)
            generate_module_file(output_dir, dataset_name, folder_name, input_dir, metadata, env_vars)

    print(f"Module files have been generated in {output_base_dir}")

if __name__ == "__main__":
    main()
