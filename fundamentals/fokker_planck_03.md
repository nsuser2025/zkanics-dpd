<p>
以上をまとめると, DPD 粒子系の Fokker-Planck 方程式は次式で表される.
ただし, 保存力項 $L_{\rm C} \rho$ と揺動散逸項 $L_{\rm D}\rho$ とした.
</p>
$$
\begin{align}
L_{\rm C}\rho({\bf r},{\bf p},t) 
&= -\sum_{i} \frac{{\bf p}_{i}}{m_{i}} \cdot \frac{\partial}{\partial {\bf r}_{i}} \rho({\bf r},{\bf p},t) 
-\sum_{i}\sum_{j \neq i} {\bf F}^{\rm C}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}} \rho({\bf r},{\bf p},t) 
\tag{11} \\
L_{\rm D}\rho({\bf r},{\bf p},t) 
&= \sum_{i}\sum_{j \neq i} \gamma \omega_{\rm D}(r_{ij}) {\bf e}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}}
 \{({\bf e}_{ij}\cdot {\bf v}_{ij})\} \\
&+\frac{1}{2} \sum_{i} \sum_{j \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij})
{\bf e}_{ij} \cdot \biggl\{ \frac{\partial}{\partial {\bf p}_{i}}
\biggl[{\bf e}_{ij} \cdot
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\rho({\bf r},{\bf p},t) \biggr] \biggr\}
\tag{12}
\end{align}
$$
<p>
平衡状態では $L_{\rm C}\rho_{\rm eq} = 0$, $L_{\rm D}\rho_{\rm eq} = 0$ が満たされている.
ここで, $\partial \rho_{\rm eq}/\partial {\bf p}_{i} = -\beta {\bf v}_{i} \rho_{\rm eq}$
より, 次式が成り立つとき $L_{\rm D}\rho_{\rm eq} = 0$ になる.
</p>
$$
\begin{align}
\gamma \omega_{\rm D}(r_{ij})({bf e}_{ij}\cdot {\bf v}_{ij})
-\beta \frac{\sigma^{2}}{2} {\bf e}_{ij} \cdot ({\bf v}_{ij}) \rho_{\rm eq} = 0
\end{align}
$$
