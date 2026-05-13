<p>
<u>Fokker-Planck 方程式</u>
</p>
$$
\begin{align}
d{\bf r}_{i} &= \frac{{\bf p}_{i}}{m_{i}} dt \tag{1} \\
d{\bf p}_{i} &= \biggl[
\sum_{i \neq j} {\bf F}^{\rm C}_{ij}(r_{ij}) 
+ \sum_{i \neq j} (-\gamma) \omega_{\rm D}(r_{ij}) ({\bf e}_{ij}\cdot{\bf v}_{ij}){\bf e}_{ij} \biggr] dt
+ \sum_{j \neq i} \sigma \omega_{\rm R}(r_{ij}) {\bf e}_{ij} dW_{ij} \tag{2}
\end{align}
$$
$$
\begin{align}
L_{\rm D}\rho({\bf r},{\bf p},t)
&= \sum_{i}\sum_{j \neq i}
{\bf e}_{ij} \frac{\partial}{\partial {\bf p}_{i}} \biggl[
\gamma \omega_{\rm D}(r_{ij}) ({\bf e}_{ij}\cdot {\bf v}_{ij}) \\
&+ \frac{\sigma^{2}}{2} \omega^{2}_{\rm R}(r_{ij}) {\bf e}_{ij}
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\biggr] \rho({\bf r},{\bf v},t)
\end{align}
$$

<p>
Ito積分
</p>
$$
\begin{align}
df &= \sum_{i}\frac{\partial f}{\partial x_{\alpha}} A_{\alpha}({\bf x},t)dt
+ \sum_{\alpha\beta} \frac{\partial f}{\partial x_{\beta}} B_{\beta\alpha} dW_{\alpha}
+ \frac{1}{2} \sum_{\alpha\beta} D_{\alpha\beta} \frac{\partial^{2}f}{\partial x_{\alpha}\partial x_{\beta}} dt
\end{align}
$$
<p>
ここで ${\bf D}$ は
</p>
$$
\begin{align}
{\bf D} &= \begin{pmatrix}
{\bf D}_{\rm rr} & {\bf D}_{\rm rp}  \\
{\bf D}_{\rm pr} & {\bf D}_{\rm pp}
\end{pmatrix}
= \begin{pmatrix}
{\bf 0} & {\bf 0}  \\
{\bf 0} & {\bf D}'
\end{pmatrix}
\end{align}
$$
<p>
${\bf D}' \equiv \sum_{j} {\bf B}^{\rm T}_{j}{\bf B}_{j}$ で,
${\bf B}_{j} \equiv ({\bf B}_{1, j}, {\bf B}_{2, j}, \cdots, {\bf B}_{N, j})$
とすると, ベクトル ${\bf B}_{i,j} \equiv \sigma \omega_{\rm R}(r_{ij}) {\bf e}_{ij}$ である.
ここで, ${\bf D}'_{ij} = \sum_{j'} {\bf B}^{\rm T}_{i,j'}{\bf B}_{j,j'}$ であるため
</p>
$$
\begin{align}
\frac{\partial^{2} {\bf D}'_{ij}}{\partial {\bf p}_{i}\partial {\bf p}_{j}}
&= \frac{\partial^{2}}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \sum_{j'} {\bf B}^{\rm T}_{i,j'}{\bf B}_{j,j'} \\
&= \frac{\partial^{2}}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \sum_{j'}
\sigma \omega_{\rm R}(r_{ij'}){\bf e}^{\rm T}_{ij'} \sigma \omega_{\rm R}(r_{jj'}){\bf e}_{jj'}
\end{align}
$$
<p>
Fokker-Planck 方程式の ${\bf D}'$ 依存項  
</p>
$$
\begin{align}
\frac{1}{2} \sum_{i,j} \frac{\partial^{2}}{\partial {\bf p}_{i}\partial {\bf p}_{j}}( {\bf D}'_{ij} 
\rho({\bf r}, {\bf p}, t))
\end{align}
$$
