#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
n = int(input('幾つの乱数?'))
s = []
for i in range (0,n):
    a = random.randint(1,100)
    s.append(a)
print(s)
def sortf(s_raw):
    pivot = len(s_raw) - 1
    global new_pivot
    for j in range (0, pivot-1):
        if s_raw[j] > s_raw[pivot]:
            for k in reversed (range(j, pivot-1)):
                if s_raw[k] < s_raw[pivot]:
                    b = s_raw[j]
                    s_raw[j] = s_raw[k]
                    s_raw[k] = b
                elif j == k:
                    c = s_raw[j]
                    s_raw[j] = s_raw[pivot]
                    s_raw[pivot] = c
                    new_pivot = j
                else:
                    pass
        else:
            pass
def fan(s):
    sortf(s)
    lefts = s[:new_pivot]
    rights = s[new_pivot+1:]
    while len(lefts) > 1:
        sortf(lefts)
        sortf(rights)
        lefts.append(new_pivot)
        s = lefts + rights
        print(s)
        return s
fan(s)
