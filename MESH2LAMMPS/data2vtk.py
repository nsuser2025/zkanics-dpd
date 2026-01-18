import numpy as np
import sys
import os

def read_lammps_data_atoms(filename):
    atoms = []
    types = []

    with open(filename) as f:
        in_atoms = False
        for line in f:
            if line.strip().startswith("Atoms"):
                in_atoms = True
                next(f)
                continue
            if in_atoms:
                if line.strip() == "":
                    break
                parts = line.split()
                types.append(int(parts[2]))
                atoms.append([float(parts[-3]),
                              float(parts[-2]),
                              float(parts[-1])])

    return np.array(atoms), np.array(types)

def write_vtk_points(filename, points, types):
    with open(filename, "w") as f:
        f.write("# vtk DataFile Version 3.0\n")
        f.write("LAMMPS particles\n")
        f.write("ASCII\n")
        f.write("DATASET POLYDATA\n")
        f.write(f"POINTS {len(points)} float\n")
        for x, y, z in points:
            f.write(f"{x} {y} {z}\n")

        f.write(f"\nPOINT_DATA {len(points)}\n")
        f.write("SCALARS type int 1\n")
        f.write("LOOKUP_TABLE default\n")
        for t in types:
            f.write(f"{t}\n")

if __name__ == "__main__":
   argv = sys.argv
   filename = argv[1]
   name = os.path.splitext(filename)[0] + '.vtk'
   points, types = read_lammps_data_atoms(filename)
   write_vtk_points(name, points, types)

