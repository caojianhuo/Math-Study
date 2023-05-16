# 简单迭代法求方程的根
import math
def f(x):
    return math.acos(math.exp(-x))
def g(a,e):
    k = 0
    print("k=",k,"x=",a)
    b = f(a)
    k = k + 1
    print("k=",k,"x=",b)
    while abs(b-a)/abs(a) > e:
        a = b
        b = f(a)
        k = k + 1
        print("k=",k,"x=",b)
    print("方程的根为：",b)
    print("迭代次数为：",k)
    print("误差为：",abs(b-a)/abs(a))

g(1.2,0.000001)