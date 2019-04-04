#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
n = int(input()) #n等分
pi = ( n / 2 ) * math.sin (math.radians(360 / n))
print(pi)
