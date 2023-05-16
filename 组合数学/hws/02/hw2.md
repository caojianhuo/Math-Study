+ eg1、求序列$0,1×2×3,2×3×4,\ldots,n(n+1)(n+2),\ldots$的母函数。

$$
\frac{1}{1-x}=1+x+x^2+\ldots
$$

$$
\frac{1}{(1-x)^2}=1+2x+3x^2+\ldots
$$

$$
\frac{2}{(1-x)^3}=2+2×3x+3×4x^2+\ldots
$$

$$
\frac{6}{(1-x)^4}=1×2×3+2×3×4x+\ldots
$$

$$
\frac{6x}{(1-x)^4}=0+1×2×3x+2×3×4x^2+\ldots
$$


+ eg2、求$n$位十进制数中出现偶数个5的数的个数。

令：

$a_n=n位十进制数中出现\textbf{偶数}个5的数的个数$

$b_n=n位十进制数中出现\textbf{奇数}个5的数的个数$
$$
\left\{  
             \begin{array}{**lr**}  
             a_n=9a_{n-1}+b_{n-1} &  \\  
             b_n=9b_{n-1}+a_{n-1} &    
             \end{array}  
\right.
$$

其中$a_1=8,b_1=1$
$$
A(x)=a_1+a_2x+a_3x^2+\ldots \\
 \\
$$




联立：
$$
\left\{  
             \begin{array}{**lr**}  
             (1-9x)A(x)-xB(x)=8 &  \\  
             (1-9x)B(x)-xA(x)=1 &    
             \end{array}  
\right.
$$
得：
$$
A(x)=\frac{8-71x}{(1-10x)(1-8x)}=\frac{9}{2(1-10x)}+\frac{7}{2(1-8x)}  \\
= \frac{9}{2}(1+10x+10^2x^2+\ldots)+\frac{7}{2}(1+8x+8^2x^2+\ldots) \\
$$
容易得到：

$a_{n+1}=\frac{9}{2}×10^n+\frac{7}{2}×8^n$


+ eg3、求序列$\{0,1,8,27,\ldots,n^3,\ldots\}$的母函数。

$$
\frac{1}{1-x}=1+x+x^2+\ldots
$$

$$
\frac{x}{(1-x)^2}=x+2x^2+3x^3+\ldots
$$

$$
\frac{1+x}{(1-x)^3}=1+2^2x+3^2x^2+\ldots
$$

$$
\frac{(1+x)x}{(1-x)^3}=x+2^2x^2+3^2x^3+\ldots
$$

$$
\frac{1+3x+2x^3}{(1-x)^4}=1+2^3x+3^3x^2+\ldots
$$

$$
\frac{x+3x^2+2x^4}{(1-x)^4}=x+2^3x^2+3^3x^3+\ldots
$$