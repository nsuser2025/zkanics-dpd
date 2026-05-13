<p>
次式の DPD 運動方程式を考える.  
</p>
$$
\begin{align}
d{\bf r}_{i} &= \frac{{\bf p}_{i}}{m_{i}} dt \tag{1} \\
d{\bf p}_{i} &= \biggl[
\sum_{j \neq i} {\bf F}^{\rm C}_{ij}(r_{ij}) 
+ \sum_{j \neq i} (-\gamma) \omega_{\rm D}(r_{ij}) ({\bf e}_{ij}\cdot{\bf v}_{ij}){\bf e}_{ij} \biggr] dt
+ \sum_{j \neq i} \sigma \omega_{\rm R}(r_{ij}) {\bf e}_{ij} dW_{ij} \\
&\equiv {\bf A}_{i} dt + \sum_{j \neq i} {\bf B}_{i,j} dW_{ij} \tag{2}
\end{align}
$$
<p>
伊藤公式より, 任意の滑らかな関数 $f$ に対し, 次式がなりたつ.
</p>
$$
\begin{align}
df &= \sum_{i} \frac{df}{d{\bf r}_{i}} d{\bf r}_{i} + \sum_{i} \frac{df}{d{\bf p}_{i}} d{\bf p}_{i} \\
&+ \frac{1}{2} \sum_{i,j} \frac{\partial^{2} f}{\partial {\bf r}_{i}\partial {\bf r}_{j}} d{\bf r}^{\rm T}_{i}d{\bf r}_{j}
+ \sum_{i,j} \frac{\partial^{2} f}{\partial {\bf r}_{i}\partial {\bf p}_{j}} d{\bf r}^{\rm T}_{i}d{\bf p}_{j}
\end{align}
$$
