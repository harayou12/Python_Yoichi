#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input('判定したい数?>'))
b = []
for j in range(2,n):
    a = []
    for i in range(1,j):
        s = j % i
        if s == 0:
            a.append(s)
        else:
            pass
    if len(a) == 1:
        b.append(j)
    else:
        pass
print(b)
