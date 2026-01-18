#### trimesh を用いた STL 作成

<p>
1. 曲面定義 </br>
2. ノード配置（vertices）</br>
3. 三角形生成（faces）</br>
4. watertight（水密性）確認.
</p>

<p>
水密性: メッシュが完全に閉じていて水が一切漏れない状態.
trimesh の is_watertight が Flase のときは次の状態が考えられる. </br>
1. 穴があいている. </br>
2. 一部の三角形が逆向きで内外を定義できない. </br>
3. 面が他の面を貫通したり, 交差している. </br>
これらの状態は非物理的なシミュレーション結果の原因になるので
かならず is_watertight を確認する.
</p>

<figure style="text-align: center;">
<img src="https://raw.githubusercontent.com/nsuser2025/zkanics-notes-on-dpd/main/MESH2LAMMPS/trimesh_helical.png" 
alt="trimesh_helical" width="200">
<figcaption style="text-align:center;">図1: シリンダー表面の仮想粒子化</figcaption>
</figure>
