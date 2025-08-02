import os
import argparse
from ase.io import read, write

def convert_sdf_to_extxyz(sdf_dir, output_file):
    open(output_file, "w").close()
    sdf_files = [f for f in os.listdir(sdf_dir) if f.endswith(".sdf")]

    if not sdf_files:
        print("No .sdf files found in the directory.")
        return

    for filename in sdf_files:
        filepath = os.path.join(sdf_dir, filename)
        try:
            atoms = read(filepath, format="sdf")
            write(output_file, atoms, format="extxyz", append=True)
            print(f"✔ Converted: {filename}")
        except Exception as e:
            print(f"⚠️ Failed to read {filename}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch convert .sdf files to .extxyz format using ASE")
    parser.add_argument("sdf_directory", help="Directory containing .sdf files")
    parser.add_argument("output_file", help="Output .extxyz filename")

    args = parser.parse_args()
    convert_sdf_to_extxyz(args.sdf_directory, args.output_file)

