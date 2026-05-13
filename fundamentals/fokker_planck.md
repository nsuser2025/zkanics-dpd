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
\gamma \omega_{\rm D}(r_{ij}) ({\bf e}_{ij}\cdot {\bf v}_{ij})
+ \frac{\sigma^{2}}{2} \omega^{2}_{\rm R}(r_{ij}) {\bf e}_{ij}
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\biggr] \rho({\bf r},{\bf v},t)
\end{align}
$$
