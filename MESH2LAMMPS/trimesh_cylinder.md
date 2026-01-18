#### trimesh を用いたシリンダーの STL 作成

<p>
三角形を並べて帯を作ると両端が斜めな平行四辺形になる.
その帯の両端をつなげて円柱を作ろうとすると両端が重なる箇所に
位相の不一致が生じて, 歪なメッシュ領域ができてしまう.
これにより, mesh2lammps は均一な粒子を置くことができなくなり,
ファスナーのような領域ができてしまう.
</p>

<figure style="text-align: center;">
<img src="https://raw.githubusercontent.com/nsuser2025/sfg-notes/main/notes/skinner_SFG.jpg" alt="Skinner_SFG" width="200">
<figcaption style="text-align:center;">図1: Skinnerらによる水界面のSFGスペクトル</figcaption>
</figure>
