import os
import argparse
from ase.io import read, write

def convert_sdf_to_extxyz(sdf_input, output_file):
    # Clear the output file
    open(output_file, "w").close()

    # Check if input is a directory or a single file
    if os.path.isdir(sdf_input):
        sdf_files = [
            os.path.join(sdf_input, f)
            for f in os.listdir(sdf_input)
            if f.endswith(".sdf")
        ]
    elif os.path.isfile(sdf_input) and sdf_input.endswith(".sdf"):
        sdf_files = [sdf_input]
    else:
        print("ERROR: Input must be a .sdf file or a directory containing .sdf files.")
        return

    # Convert each file
    for filepath in sdf_files:
        try:
            atoms = read(filepath, format="sdf")
            write(output_file, atoms, format="extxyz", append=True)
            print(f"Converted: {filepath}")
        except Exception as e:
            print(f"Failed to read {filename}: {e}")
            print(f"ERROR: Could not process {filepath}\n{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .sdf files to .extxyz format using ASE")
    parser.add_argument("sdf_input", help="Path to a single .sdf file or a folder containing .sdf files")
    parser.add_argument("output_file", help="Name of the output .extxyz file")
    args = parser.parse_args()

    convert_sdf_to_extxyz(args.sdf_input, args.output_file)

