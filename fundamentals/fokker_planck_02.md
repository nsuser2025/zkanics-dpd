<p>
ここで $dW_{ij}=dW_{ji}$ を満たす独立なウィーナー過程とすると,
式 4 の第二項は,
$dW_{ij'}dW_{jj''} = (\delta_{ij}\delta_{j'j''} + \delta_{ij''}\delta_{j'j}) dt$
より, 次式で表される.(Ref. Espanol1995 Eq. 5)
</p>
$$
\begin{align}
&\frac{1}{2} \sum_{i,j}\sum_{j' \neq i}\sum_{j'' \neq j} 
\biggl[({\bf B}_{i,j'} \otimes {\bf B}_{j,j''})
:: \frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \biggr] dW_{ij'}dW_{jj''} \\
&= \frac{1}{2} \sum_{i,j}\sum_{j' \neq i}\sum_{j'' \neq j}
\biggl[ ({\bf B}_{i,j'} \otimes {\bf B}_{j,j''})
:: \frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \biggr]
(\delta_{ij}\delta_{j'j''} + \delta_{ij''}\delta_{j'j}) dt \\
&= \frac{1}{2} \sum_{i} \sum_{j' \neq i} \biggl[
({\bf B}_{i,j'} \otimes {\bf B}_{i,j'})
:: \frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{i}} \biggr] dt
+ \frac{1}{2} \sum_{i,j} \biggl[ ({\bf B}_{i,j} \otimes {\bf B}_{j,i})
:: \frac{\partial^{2} f}{\partial {\bf p}_{i}\partial {\bf p}_{j}} \biggr] dt \tag{6}
\end{align}
$$
<p>
式 6 に対応する Fokker-Planck 方程式の項はそれぞれ次式で表される. 
ただし, $i = j$ 項は DPD はゼロになることを考慮した.
</p>
$$
\begin{align}
&\frac{1}{2} \sum_{i} \sum_{j' \neq i} \frac{\partial}{\partial {\bf p}_{i}}
\cdot \biggl[({\bf B}_{i,j'} \otimes {\bf B}_{i,j'}) \frac{\partial}{\partial {\bf p}_{i}} \rho({\bf r},{\bf p},t)\biggr] \\
&= \frac{1}{2} \sum_{i} \sum_{j' \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij'}) \frac{\partial}{\partial {\bf p}_{i}}
\cdot \biggl[({\bf e}_{ij'} \otimes {\bf e}_{ij'}) 
\frac{\partial}{\partial {\bf p}_{i}} \rho({\bf r},{\bf p},t) \biggr] \tag{7} \\
&\frac{1}{2} \sum_{ij} \frac{\partial}{\partial {\bf p}_{i}} \cdot
\biggl[ ({\bf B}_{i,j} \otimes {\bf B}_{j,i}) \frac{\partial}{\partial {\bf p}_{j}} \rho({\bf r},{\bf p},t) \biggr] \\
&= \frac{1}{2} \sum_{ij} \sigma^{2}\omega^{2}_{\rm R}(r_{ij}) \frac{\partial}{\partial {\bf p}_{i}}
\cdot \biggl[({\bf e}_{ij}\otimes{\bf e}_{ji}) \frac{\partial}{\partial {\bf p}_{j}} \rho({\bf r},{\bf p},t) \\
&= -\frac{1}{2} \sum_{i}\sum_{j \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij}) \frac{\partial}{\partial {\bf p}_{i}}
\cdot \biggl[ ({\bf e}_{ij}\otimes{\bf e}_{ij}) \frac{\partial}{\partial {\bf p}_{j}} \rho({\bf r},{\bf p},t)\biggr] \tag{8}
\end{align}
$$
<p>
以上より, 揺動力に起因する Fokker-Planck 方程式の項は次式となる.  
</p>
$$
\begin{align}
\frac{1}{2} \sum_{i} \sum_{j \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij})
\frac{\partial}{\partial {\bf p}_{i}} \cdot
\biggl[ ({\bf e}_{ij} \otimes {\bf e}_{ij}) 
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\rho({\bf r},{\bf p},t) \biggr] \tag{9}
\end{align}
$$
<p>
ここで $({\bf a} \otimes {\bf b}){\bf X} = {\bf a}({\bf b}\cdot {\bf X})$ より, 
</p>
$$
\begin{align}
\frac{1}{2} \sum_{i} \sum_{j \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij})
\frac{\partial}{\partial {\bf p}_{i}} \cdot
\biggl\{ {\bf e}_{ij} \biggl[{\bf e}_{ij} \cdot
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\rho({\bf r},{\bf p},t) \biggr] \biggr\} 
\end{align}
$$
<p>
ここで $[\cdots]$ はスカラーで, $\partial {\bf e}_{ij}/\partial {\bf p}_{i} = 0$
であることから, 次式が成り立つことを考慮する.
</p>
$$
\begin{align}
\frac{\partial}{\partial {\bf p}_{i}} \cdot ({\bf {e}}_{ij}[\cdots])
&= {\bf {e}}_{ij} \cdot \frac{\partial}{\partial {\bf p}_{i}} ([\cdots])
\end{align}
$$
<p>
最終的な Fokker-Planck 方程式の揺動力項は次式で表される.  
</p>
$$
\begin{align}
\frac{1}{2} \sum_{i} \sum_{j \neq i} \sigma^{2}\omega^{2}_{\rm R}(r_{ij})
{\bf e}_{ij} \cdot \biggl\{ \frac{\partial}{\partial {\bf p}_{i}}
\biggl[{\bf e}_{ij} \cdot
\biggl( \frac{\partial}{\partial {\bf p}_{i}} - \frac{\partial}{\partial {\bf p}_{j}} \biggr)
\rho({\bf r},{\bf p},t) \biggr] \biggr\} \tag{10} 
\end{align}
$$
