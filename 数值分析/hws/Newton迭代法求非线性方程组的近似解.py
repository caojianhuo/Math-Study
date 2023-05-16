import numpy as np
import math
def f(x):
    return np.array([x[0]-math.sin(x[1]+x[0])-1.2,x[1]+math.cos(x[0]+x[1])-0.5]) # 方程组
def J(x):
    return np.array([[1-math.cos(x[0]+x[1]),-math.cos(x[0]+x[1])],[-math.sin(x[0]+x[1]),1-math.sin(x[0]+x[1])]]) # 方程组的雅可比矩阵
def g(x,e):
    k = 0
    print("k=",k,"x=",x)
    b = x - np.dot(np.linalg.inv(J(x)),f(x))
    k = k + 1
    print("k=",k,"x=",b)
    while np.linalg.norm(b-x,np.inf) > e:
        x = b
        b = x - np.dot(np.linalg.inv(J(x)),f(x))
        k = k + 1
        print("k=",k,"x=",b)
    print("方程组的近似解为：",b)
    print("迭代次数为：",k)
    print("误差为：",np.linalg.norm(b-x,np.inf))
g(np.array([1,1]),0.0001)