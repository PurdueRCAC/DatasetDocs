#!/usr/bin/env python3

from generate_docs import parse_lua_file, clean_help_text, generate_rst_file
from pathlib import Path

def main():
    # Parse the sample file
    help_text, envvars = parse_lua_file(Path("sample.lua"))
    
    # Generate a test RST file
    generate_rst_file(
        category="geospatial",
        dataset_name="MERIT_Hydro",
        version="2019-05-28",
        help_text=help_text,
        envvars=envvars,
        output_file=Path("test_output.rst")
    )
    
    # Print the contents of the generated file
    print("=== Generated RST File ===")
    print(Path("test_output.rst").read_text())

if __name__ == "__main__":
    main() 