# Python_Yoichi
#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input('幾つのソート?>'))
xmax = int(input('最大値>'))
xmin = int(input('最小値>'))
S = 0
dx = xmax - xmin
def f(x):
    return (x ** 2 + x * (1 + x ** 2) ** (- 1/2)) * (1 + x * (1 + x ** 2) ** (- 3/2))
for i in range(0,n):
    S += (1 / n) * f(xmin + i * dx / n)
print(S)
