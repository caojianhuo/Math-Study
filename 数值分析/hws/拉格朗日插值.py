def lagrange_interpolation(points):
    def basis_polynomial(k, x):
        result = 1
        for i, point in enumerate(points):
            if i != k:
                result *= (x - point[0]) / (points[k][0] - point[0])
        return result

    def lagrange_polynomial(x):
        result = 0
        for k, point in enumerate(points):
            result += point[1] * basis_polynomial(k, x)
        return result

    return lagrange_polynomial

# 输入点的数量
n = int(input("请输入点的数量："))

# 输入点的坐标
points = []
for i in range(n):
    x = float(input(f"请输入第 {i+1} 个点的 x 坐标："))
    y = float(input(f"请输入第 {i+1} 个点的 y 坐标："))
    points.append((x, y))

# 调用拉格朗日插值函数，得到拟合的多项式
interpolation = lagrange_interpolation(points)

from sympy import symbols, expand

# 创建符号变量
x = symbols('x')

# 获取拟合的多项式表达式
expression = ""
for k, point in enumerate(points):
    term = f"({point[1]})"
    for i, p in enumerate(points):
        if i != k:
            term += f" * (x - {p[0]}) / ({point[0]} - {p[0]})"
    expression += term + " + "

expression = expression[:-3]  # 去掉最后一个 "+"

# 将多项式表达式化简
simplified_expression = expand(expression)

# 打印拟合的多项式表达式（最简式）
print("拟合的多项式为（最简式）：")
print(simplified_expression)



