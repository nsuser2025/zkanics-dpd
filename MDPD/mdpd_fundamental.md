<p>
通常の単一成分系 DPD 流体の状態方程式（EOS）は $\rho$ の二次関数で近似される: 
</p>
$$
\begin{align}
p &= \rho k_{\rm B}T + \alpha a_{ij}\rho^{2} \tag{1}
\end{align}
$$
<p>
この EOS には van der Waals ループが含まれていないため,
気液共存や自由表面を伴う現象をシミュレーションすることはできない.
MDPD では保存力を粒子間距離だけでなく, その瞬間の局所粒子密度にも依存させることで EOS に高次項を導入している.
それにより, MDPD における保存力は実質的に多体力となり, 一般に引力成分と斥力成分の両方を含む.
EOS に高次項が導入されたことで, MDPD は液滴形成や濡れに関連する現象のシミュレーションが可能となる. 
MDPD の保存力は次式で表される（ただし, 散逸力と揺動力は通常の DPD simulation と同じである）:
</p>
<p><u>保存力</u></p>
$$
\begin{align}
{\bf F}_{ij}^{\rm c} &= a_{ij} \omega_{\rm c}(r_{ij}) {\bf e}_{ij} 
+ b_{ij} ({\bar \rho}_{i} + {\bar \rho}_{j}) \omega_{\rm d}(r_{ij}) {\bf e}_{ij} \tag{2} \\
{\bar \rho}_{i} &= \sum_{i \neq j} \omega_{\rho}(r_{ij}) \tag{3} \\
\omega_{\rm c}(r_{ij}) &= \biggl(1-\frac{r_{ij}}{r_{\rm c}} \biggr) 
\hspace{0.4cm}\text{for $r_{ij} \le r_{\rm c}$} \tag{4} \\
\omega_{\rm d}(r_{ij}) &= \biggl(1-\frac{r_{ij}}{r_{\rm d}} \biggr) 
\hspace{0.4cm}\text{for $r_{ij} \le r_{\rm d}$} \tag{5} \\ 
\omega_{\rho}(r_{ij}) &= \frac{15}{2\pi r_{\rm d}^{3}} \biggl( 
1 - \frac{r_{ij}}{r_{\rm d}} \biggr)^{2} \text{for $r_{ij} \le r_{\rm d}$} \tag{6} \\
\int_{0}^{\infty} 4\pi r^{2} \omega_{\rho}(r) dr 
&= \frac{30}{r_{\rm d}^{3}}\biggl( \frac{r_{\rm d}^{3}}{3} 
- \frac{r_{\rm d}^{4}}{2r_{\rm d}} + \frac{r_{\rm d}^{5}}{5r_{\rm d}^{2}} \biggr)
= 30 \biggl( \frac{1}{3} - \frac{1}{2} + \frac{1}{5} \biggr) = 1 \tag{7}
\end{align}
$$
<p>
2 の第二項が無ければ soft-core potential と同じである.
つまり, $a_{ij}$ はカイパラメータから決めることができるものであるが,
MDPD では適当に決められていることが多い.
</p>
