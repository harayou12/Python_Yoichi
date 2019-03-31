#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math
p = int(input()) #p回試行
n = int(input()) #n等分
pn = 0
for i in range(1,p):
    x = random.random()
    y = random.random()
    s  = ( x ** 2 + y ** 2 ) / n
    if s < 1:
        pn += 1
    elif s >= 1:
        pn += 0
pi = (pn / p) * n * math.tan (math.radians(180 / n))
print(pi)
