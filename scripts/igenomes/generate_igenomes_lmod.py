#!/usr/bin/env python3
import os
import sys
import datetime

def ensure_trailing_slash(rel_path, full_path):
    """Append a trailing slash to rel_path if full_path is a directory."""
    if os.path.isdir(full_path) and not rel_path.endswith("/"):
        return rel_path + "/"
    return rel_path

def find_existing_path(modroot, candidates):
    """
    Given a list of candidate relative paths (or a single candidate string),
    return the first candidate that exists. If found, return a tuple of the
    candidate and its full path. Otherwise return (None, None).
    """
    if isinstance(candidates, str):
        candidates = [candidates]
    for rel in candidates:
        full = os.path.join(modroot, rel)
        if os.path.exists(full):
            return rel, full
    return None, None

def is_release_dir(directory):
    """
    Determine if the given directory qualifies as a genome release directory
    by checking for the existence of both the 'Sequence' and 'Annotation' subdirectories.
    """
    return (os.path.isdir(os.path.join(directory, "Sequence")) and
            os.path.isdir(os.path.join(directory, "Annotation")))

def find_release_dirs(org_dir):
    """
    Given an organism directory, search for valid genome release directories.
    This function first checks the organism directory itself and then its immediate
    children (and one level deeper) for directories that contain both a 'Sequence'
    and an 'Annotation' folder.
    """
    releases = []
    if is_release_dir(org_dir):
        releases.append(org_dir)
    else:
        for child in os.listdir(org_dir):
            child_path = os.path.join(org_dir, child)
            if os.path.isdir(child_path):
                if is_release_dir(child_path):
                    releases.append(child_path)
                else:
                    for subchild in os.listdir(child_path):
                        subchild_path = os.path.join(child_path, subchild)
                        if os.path.isdir(subchild_path) and is_release_dir(subchild_path):
                            releases.append(subchild_path)
    return releases

def generate_module(modroot, version_date):
    """
    Generate the Lua module file content for a given genome release directory (modroot).
    It looks for expected files or directories relative to modroot (e.g. Sequence/WholeGenomeFasta/genome.fa,
    Annotation/Genes/genes.gtf, etc.) and only emits setenv() lines for items that exist.
    """
    build_name = os.path.basename(os.path.normpath(modroot))

    # Expected keys: each maps to a tuple (candidate path(s), type: "file" or "dir")
    expected = {
        "fasta":   ("Sequence/WholeGenomeFasta/genome.fa", "file"),
        "bwa":     (["Sequence/BWAIndex/version0.6.0", "Sequence/BWAIndex/version0.5.x"], "dir"),
        "bowtie2": ("Sequence/Bowtie2Index", "dir"),
        "star":    ("Sequence/STARIndex", "dir"),
        "bismark": ("Sequence/BismarkIndex", "dir"),
        "gtf":     ("Annotation/Genes/genes.gtf", "file"),
        "bed12":   ("Annotation/Genes/genes.bed", "file"),
        "readme":  ("Annotation/README.txt", "file")
    }

    found_env = {}
    for key, (rel_candidates, typ) in expected.items():
        rel_found, full_found = find_existing_path(modroot, rel_candidates)
        if rel_found:
            # Convert to Lua concatenation style: always with a leading slash
            rel_path = "/" + rel_found.replace(os.sep, "/")
            if typ == "dir":
                rel_path = ensure_trailing_slash(rel_path, full_found)
            found_env[key] = rel_path

    # Fixed variables to always include
    fixed_vars = {
        "HOME": modroot
    }

    # RCAC-specific variables
    rcac_vars = {
        "ROOT": modroot,
        "VERSION": version_date
    }

    # Build the Lua file content.
    lines = []
    lines.append("help([[")
    lines.append(f"The contents of this lmod file were automatically generated on: {datetime.date.today().strftime('%Y-%m-%d')}.")
    lines.append("]])")
    lines.append(f'local modroot="{modroot}"')
    
    # Emit setenv lines for found items (named as <build_name>_<key>)
    for key in sorted(found_env.keys()):
        lines.append(f'setenv("{build_name}_{key}", modroot.."{found_env[key]}")')
    
    # Fixed variables
    for key, value in fixed_vars.items():
        lines.append(f'setenv("{build_name}_{key}", "{value}")')
    
    # RCAC variables (named as RCAC_<build_name>_KEY)
    for key, value in rcac_vars.items():
        lines.append(f'setenv("RCAC_{build_name}_{key}", "{value}")')

    return "\n".join(lines) + "\n"

def main():
    if len(sys.argv) < 2:
        print("Usage: {} <igenomes_directory>".format(sys.argv[0]))
        sys.exit(1)

    top_dir = os.path.abspath(sys.argv[1])
    if not os.path.isdir(top_dir):
        print("Error: {} is not a valid directory.".format(top_dir))
        sys.exit(1)

    # Define the output base directory (relative to the current working directory).
    output_base = os.path.join(os.getcwd(), "igenomes_lua")
    os.makedirs(output_base, exist_ok=True)

    version_date = datetime.date.today().strftime("%Y-%m-%d")
    count = 0

    # Process each organism directory within the top-level igenomes directory.
    for organism in os.listdir(top_dir):
        org_path = os.path.join(top_dir, organism)
        if not os.path.isdir(org_path):
            continue

        # Find genome release directories within this organism.
        release_dirs = find_release_dirs(org_path)
        if not release_dirs:
            print(f"No valid genome release found for organism: {organism}")
            continue

        for modroot in release_dirs:
            # Determine the release name as the leaf of modroot.
            release_name = os.path.basename(os.path.normpath(modroot))
            # Build output directory: output_base/organism/release_name
            out_dir = os.path.join(output_base, organism, release_name)
            os.makedirs(out_dir, exist_ok=True)

            module_content = generate_module(modroot, version_date)
            # Write the Lua module file into the output directory.
            out_file = os.path.join(out_dir, f"{version_date}.lua")
            with open(out_file, "w") as f:
                f.write(module_content)
            print(f"Wrote Lua module for {modroot} -> {out_file}")
            count += 1

    print(f"Generated Lua module file(s) for {count} genome release(s).")

if __name__ == "__main__":
    main()
