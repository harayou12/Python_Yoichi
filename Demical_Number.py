#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = int(input())
sho = 0
amari = 0
b = []
while a > 0:
    amari = a % 2
    b.append(amari)
    a = a // 2
print(b)
