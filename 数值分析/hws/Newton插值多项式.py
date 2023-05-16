import numpy as np

def calculate_difference_quotients(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])

    return table

def calculate_newton_interpolation_polynomial(x, y, table):
    n = len(x)
    x_values = [symbol for symbol in x]
    polynomial = y[0]

    for i in range(1, n):
        term = table[0][i]
        for j in range(i):
            term *= (x_values - x[j])
        polynomial += term

    return polynomial

# 输入坐标
x = np.array([-2, -1.5, 0.5, 1, 1.5])
y = np.array([21,  23, 22, 21, 20])

# 建立差商表
difference_quotients_table = calculate_difference_quotients(x, y)

# 计算四次Newton插值多项式
polynomial = calculate_newton_interpolation_polynomial(x, y, difference_quotients_table)

# 打印差商表
print("差商表：")
print(difference_quotients_table)

# 打印四次Newton插值多项式
print("\n四次Newton插值多项式：")
print(polynomial)
