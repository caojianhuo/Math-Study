import math
def f(x):
    return math.sin(x) + x - 1
# 对分法求方程的根
def dichotomy(a, b, e):
    while (b - a)/2 > e:
        print("a = ", a, "b = ", b, "e = ", e)
        print("f(a) = ", f(a), "f(b) = ", f(b))
        c = (a + b) / 2
        print("c = ", c, "f(c) = ", f(c))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
print(dichotomy(0, 1, 0.001))
