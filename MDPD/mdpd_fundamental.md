<p>
通常の単一成分系 DPD 流体の状態方程式（EOS）は 密度 $\rho$ の二次関数で近似される
（Ishizuka2023_J.Mol.Liq.vol384.122246.Eq.16）.
この EOS では, 通常のパラメータ範囲において $(\partial p/\partial \rho)_{T} > 0$ が維持され,
相分離に特徴的な不安定性 $(\partial p/\partial \rho)_{T} < 0$ の領域が現れない. 
そのため, 通常の DPD では自発的な気液相分離を再現することはできない.
そこで, MDPD では保存力を粒子間距離だけでなく, その瞬間の局所粒子密度にも依存させることで,
適切なパラメータ設定によって $(\partial p/\partial \rho)_{T} < 0$ の領域が出現するように
EOS に高次項を導入した. 
</p>
<p>
MDPD の保存力は斥力成分（$A_{ij}$ 項）と引力成分（$B_{ij}$ 項）の両方を含む多体力である.
EOS に高次項が導入されたことで, 液滴形成や濡れに関連する現象のシミュレーションが可能になる. 
MDPD の保存力は次式で表される（散逸力と揺動力は通常の DPD simulation と同じである）:
</p>
$$
\begin{align}
{\bf F}_{ij}^{\rm C} &= A_{ij} \omega_{\rm c}(r_{ij}) {\bf e}_{ij} 
+ B_{ij} ({\bar \rho}_{i} + {\bar \rho}_{j}) \omega_{\rm d}(r_{ij}) {\bf e}_{ij} \tag{1} \\ \\
{\bf F}_{ij}^{\rm D} &= -\gamma \omega_{\rm c}^{2}(r_{ij})
({\hat {\bf r}}\cdot{\bf v}_{ij}) {\hat{\bf r}_{ij}} \tag{2} \\ \\
{\bf F}_{ij}^{\rm R} &= \sqrt{2\gamma k_{\rm B}T} \theta (\Delta t)^{1/2} 
\omega_{\rm c}(r_{ij}) {\hat{\bf r}_{ij}} \tag{3} \\ \\
{\bar \rho}_{i} &= \sum_{i \neq j} \omega_{\rho}(r_{ij}) \tag{4} \\ \\
\omega_{\rm c}(r_{ij}) &= \biggl(1-\frac{r_{ij}}{r_{\rm c}} \biggr) 
\hspace{0.4cm}\text{for $r_{ij} \le r_{\rm c}$} \tag{5} \\ \\
\omega_{\rm d}(r_{ij}) &= \biggl(1-\frac{r_{ij}}{r_{\rm d}} \biggr) 
\hspace{0.4cm}\text{for $r_{ij} \le r_{\rm d}$} \tag{6} \\ \\
\omega_{\rho}(r_{ij}) &= \frac{15}{2\pi r_{\rm d}^{3}} \biggl( 
1 - \frac{r_{ij}}{r_{\rm d}} \biggr)^{2} 
\hspace{0.4cm}\text{for $r_{ij} \le r_{\rm d}$} \tag{7} \\ \\
\int_{0}^{\infty} 4\pi r^{2} \omega_{\rho}(r) dr 
&= \frac{30}{r_{\rm d}^{3}}\biggl( \frac{r_{\rm d}^{3}}{3} 
- \frac{r_{\rm d}^{4}}{2r_{\rm d}} + \frac{r_{\rm d}^{5}}{5r_{\rm d}^{2}} \biggr)
= 30 \biggl( \frac{1}{3} - \frac{1}{2} + \frac{1}{5} \biggr) = 1 \tag{8}
\end{align}
$$
