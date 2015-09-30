#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log, sin, sqrt, cos

x = float(input("x? "))
c = cos(2 * x)
s = sin(3 * x)

if x > 7.7:
    y = log(x) * s
elif x == 7.7:
    y = ((x * x * x * x * x) - 1)**1/5
else:
    y = 1 + (c * c * c) - (3 * (s * s))

print(y)
    
