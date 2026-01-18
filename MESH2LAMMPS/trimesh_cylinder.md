#### trimesh を用いた STL 作成

<p>
作成フロー: </br>
1. 曲面定義 </br>
2. ノード配置（vertices）</br>
3. 三角形生成（faces）</br>
4. watertight（水密性）確認.
</p>

<p>
水密性: </br>
メッシュが完全に閉じていて水が一切漏れない状態.
trimesh の is_watertight が Flase のときは次の状態が考えられる. </br>
1. 穴があいている. </br>
2. 一部の三角形が逆向きで内外を定義できない. </br>
3. 面が他の面を貫通したり, 交差している. </br>
これらの状態は非物理的なシミュレーション結果の原因になるので
かならず is_watertight を確認する.
</p>

---

#### trimesh を用いたキャップなしシリンダーの STL 作成

<p>
trimesh_cylinder (radius, height, n_theta, n_z, twist_ratio) : </br>
radius: 円柱半径（def. 10.0）　</br>
height: 円柱の高さ（z-axis）（def. 20.0）</br>
n_theta: 円周のグリッド数（def. 64, 偶数にする）</br>
n_z: z-axis のグリッド数　(def. 40) </br>
twist_ratio: ずらし角度（def. 0.5）</br>
</p>

<p>
vid(i,j): vertices index（i は円周, j は z-axis のインデックス）. </br>
vid(i,j) = j * n_theta + (i % n_theta) </br>
1 層目は j = 0　で n_theta 点のノードが配置されているので, 2層目（j = 1）のときは
n_theta + 1 からインデックスが開始される. (i % n_theta) は i = n_theta のときだけ 0　になる.
これは dtheta = 2 * np.pi / n_theta（i = 0〜n_theta - 1 のグリッドが円周上に配置）より
i = n_theta は i = 0 と一致することによる.
</p>

<figure style="text-align: center;">
<img src="https://raw.githubusercontent.com/nsuser2025/zkanics-notes-on-dpd/main/MESH2LAMMPS/trimesh_helical.png" 
alt="trimesh_helical" width="200">
<figcaption style="text-align:center;">図1: シリンダー表面の仮想粒子化</figcaption>
</figure>
