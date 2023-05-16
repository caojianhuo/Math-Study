# 割线法求方程的根
import math
def f(x):
    return x+math.sin(x)-1
def g(a,b,e):
    k = -1
    print("k=",k,"x=",a)
    k = k + 1
    print("k=",k,"x=",b)
    while abs(b-a)/abs(b) > e:
        temp = b
        b = b - f(b)*(b-a)/(f(b)-f(a))
        a = temp
        k = k + 1
        print("k=",k,"x=",b)
    print("方程的根为：",b)
    print("迭代次数为：",k)
    print("误差为：",abs(b-a)/abs(a))
def h(a,b,e):
    k = 0
    print("k=",k,"x=",a)
    k = k + 1
    before = a
    print("k=",k,"x=",b)
    while abs(b-before)/abs(b) > e:
        before = b
        b = b - f(b)*(b-a)/(f(b)-f(a))
        k = k + 1
        print("k=",k,"x=",b)
    print("方程的根为：",b)
    print("迭代次数为：",k)
    print("误差为：",abs(b-before)/abs(b))
h(0,1,0.000001)
