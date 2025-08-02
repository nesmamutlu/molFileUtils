# molFileUtils

Tools for converting molecular structure files.  
This tool converts `.sdf` files into `.extxyz` format using ASE, while automatically:

- Centering each molecule in a cubic box
- Labeling each structure using the SDF file name (e.g., `mol_12345.sdf` → `label=mol_12345`)

---

#Usage

#Convert a single SDF file:
```bash
python sdf_to_extxyz.py path/to/your_file.sdf
