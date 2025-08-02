import os
import argparse
from ase.io import read, write
from ase import Atoms

def convert_sdf_to_extxyz(sdf_input, output_file=None):
    if output_file is None:
        base = os.path.splitext(os.path.basename(sdf_input))[0] if os.path.isfile(sdf_input) else "converted"
        output_file = base + ".extxyz"

    open(output_file, "w").close()

    if os.path.isdir(sdf_input):
        sdf_files = [os.path.join(sdf_input, f) for f in os.listdir(sdf_input) if f.endswith(".sdf")]
    elif os.path.isfile(sdf_input) and sdf_input.endswith(".sdf"):
        sdf_files = [sdf_input]
    else:
        print("ERROR: Input must be a .sdf file or a folder containing .sdf files.")
        return

    for filepath in sdf_files:
        try:
            atoms_list = read(filepath, format="sdf", index=":")
            if isinstance(atoms_list, Atoms):
                atoms_list = [atoms_list]

            # Get label from file name (e.g., mol_12345.sdf -> mol_12345)
            label_name = os.path.splitext(os.path.basename(filepath))[0]

            for atoms in atoms_list:
                atoms.center(vacuum=0.0)
                atoms.info["label"] = label_name

            write(output_file, atoms_list, format="extxyz", append=True)
            print(f"Converted and labeled with '{label_name}': {filepath}")

        except Exception as e:
            print(f"ERROR: Could not process {filepath}\n{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert .sdf file(s) to .extxyz using ASE, center and label molecules by file name.")
    parser.add_argument("sdf_input", help="A single .sdf file or a folder containing .sdf files")
    parser.add_argument("output_file", nargs="?", help="Optional: name of output .extxyz file")
    args = parser.parse_args()

    convert_sdf_to_extxyz(args.sdf_input, args.output_file)

