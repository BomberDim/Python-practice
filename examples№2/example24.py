#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, tan, sqrt, exp

x = float(input("x? "))

if x < 2:
    y = (6 * sin(x) - (x * x)) / 3
elif 2 <= x < 4:
    y = (exp((3 * x) - cos(2 * x))) / (3 + (4 * x * x * x * x * x * x))
else:
    y = ((6 * x * x * x) - (4 * tan(x + 1)))**1/5
    
print(y)

