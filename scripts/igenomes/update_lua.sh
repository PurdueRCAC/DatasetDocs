#!/bin/bash

# Check that two arguments (input and output directories) are provided.
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_igenomes_folder> <output_igenomes_lua_folder>"
  exit 1
fi

input_dir="$1"
output_dir="$2"

# Loop over every Lua file in the input folder.
for file in "$input_dir"/*/*.lua; do
  # Get the version folder name (e.g., AGPv3) from the Lua file path.
  version=$(basename "$(dirname "$file")")
  echo "Processing version: $version"

  # Search recursively in the output folder for a directory matching the version.
  target=$(find "$output_dir" -type d -name "$version")
  
  if [ -n "$target" ]; then
    # Determine the Lua file name from the input.
    new_lua=$(basename "$file")
    
    # Copy the new file into the found target directory.
    cp "$file" "$target/$new_lua"
    echo "Copied $file to $target/$new_lua"

    # Now remove any other Lua files in that target directory.
    for oldfile in "$target"/*.lua; do
      if [ "$(basename "$oldfile")" != "$new_lua" ]; then
         rm "$oldfile"
         echo "Deleted old file $oldfile"
      fi
    done
  else
    echo "No matching folder found for version: $version in $output_dir"
  fi
done
