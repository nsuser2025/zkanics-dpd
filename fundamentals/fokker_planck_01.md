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
伊藤公式より, 任意の滑らかな関数 $f$ に対し, 次式が成り立つ.
</p>
$$
\begin{align}
df &= \sum_{i} \frac{df}{d{\bf r}_{i}} \cdot d{\bf r}_{i} 
+ \sum_{i} \frac{df}{d{\bf p}_{i}} \cdot d{\bf p}_{i} + \frac{1}{2} \sum_{i,j} (d{\bf r}_{i} \otimes d{\bf r}_{j}) 
:: \frac{\partial^{2} f}{\partial {\bf r}_{i} \partial {\bf r}_{j}} \\
&+ \sum_{i,j} (d{\bf r}_{i} \otimes d{\bf p}_{j}) :: \frac{\partial^{2} f}{\partial {\bf r}_{i}\partial {\bf p}_{j}}
+ \frac{1}{2} \sum_{i,j} (d{\bf p}_{i} \otimes d{\bf p}_{j})
:: \frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \tag{3}
\end{align}
$$
<p>
式 3 に式 1, 2 を代入し, $dt^{2}$ 項と 1 次の $dW$ 項を無視すると, 次式が得られる.
</p>
$$
\begin{align}
df &= \sum_{i} \frac{df}{d{\bf r}_{i}} \cdot \frac{{\bf p}_{i}}{m_{i}} dt
+ \sum_{i} \frac{df}{d{\bf p}_{i}} \cdot {\bf A}_{i}dt \\
&+ \frac{1}{2} \sum_{i,j}\sum_{j' \neq i}\sum_{j'' \neq j}
\biggl[({\bf B}_{i,j'}\otimes{\bf B}_{j,j''}) ::  
\frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \biggr]
dW_{ij'}dW_{jj''} \tag{4}
\end{align}
$$
<p>
ハミルトニアン項（第一項）と散逸項（第二項）に相当する Fokker-Planck 方程式の各項は次式で表される.  
</p>
$$
\begin{align}
&-\sum_{i} \frac{{\bf p}_{i}}{m_{i}} \cdot \frac{\partial}{\partial {\bf r}_{i}} \rho({\bf r},{\bf p},t) 
-\sum_{i}\sum_{j \neq i} {\bf F}^{\rm C}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}} \rho({\bf r},{\bf p},t) \\
&+ \sum_{i}\sum_{j \neq i} \gamma \omega_{\rm D}(r_{ij}) {\bf e}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}}
 \{({\bf e}_{ij}\cdot {\bf v}_{ij})\} \tag{6}
\end{align}
$$
<p>
ここで $[\cdots]$ はスカラーとしたとき, $\partial {\bf e}_{ij}/\partial {\bf p}_{i} = 0$
であることから, 次式が成り立つことを考慮した.
</p>
$$
\begin{align}
\frac{\partial}{\partial {\bf p}_{i}} \cdot ({\bf {e}}_{ij}[\cdots])
&= {\bf {e}}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}} ([\cdots])
\end{align}
$$
