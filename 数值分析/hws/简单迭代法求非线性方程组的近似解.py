# 简单迭代法求非线性方程组的近似解
import numpy as np
def f1(x2):
    return 1.2-np.exp(-2*x2)

def f2(x1):
    return (1.97-np.exp(-x1))/2

def Solution(a,b,e):
    print("k=",0,"x1=",a,"x2=",b)
    x1 = f1(b)
    x2 = f2(a)
    k = 1
    print("k=",k,"x1=",x1,"x2=",x2)
    while abs(x1-a)/abs(x1) > e or abs(x2-b)/abs(x1) > e:
        a = x1
        b = x2
        x1 = f1(b)
        x2 = f2(a)
        k = k + 1
        print("k=",k,"x1=",x1,"x2=",x2)
    print("方程的根为：",x1,x2)
    print("迭代次数为：",k)
    print("误差为：",abs(x1-a)/abs(x1),abs(x2-b)/abs(x2))

Solution(0.5,0.5,0.0005)