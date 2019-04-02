#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = int(input('幾つのソート?>'))
b = int(input('幾つのソート?>'))
p = [a, b]
q = 0
for i in range (0,10):
    q = p[i] % p[i+1]
    if q != 0:
        p.append(q)
    elif q == 0:
        print(p[i+1])
        exit
