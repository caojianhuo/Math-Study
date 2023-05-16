#  Steffen's iteration method
#  用Steffen的迭代方法求方程的根
import math
def f(x):
    return (2-math.exp(x))/10
def g(a,e):
    k = 0
    print("k=",k,"x=",a)
    b = a
    y = f(a)
    z = f(y)
    k = k + 1
    a = a - (y-a)**2/(z-2*y+a)
    print("k=",k,"x=",a)
    while abs(b-a)/abs(a) > e:
        b = a
        y = f(a)
        z = f(y)
        a = a - (y-a)**2/(z-2*y+a)
        k = k + 1
        print("k=",k,"x=",a)
    print("方程的根为：",a)
    print("迭代次数为：",k)
    print("误差为：",abs(a-b)/abs(a))
g(0.2,0.000001)