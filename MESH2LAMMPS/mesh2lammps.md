#### インストール
<p>
conda install conda-forge::trimesh </br>
conda install conda-forge::networkx </br>
conda install scipy </br>
conda install -c conda-forge "pyglet<2"
</p>

<p>
mesh2lammps-master/src/mesh2lammps.py と lammps2mesh.py の末尾に下記を追記する. </br></br>
if __name__ == "__main__":</br>
  main()</br>
</p>

