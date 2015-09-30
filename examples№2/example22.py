#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, cos, sin, tan, log

x = float(input("x? "))

if x > 0:
    y = 3 * sqrt(x) - (x * x * x * x * cos(2 * x))
elif x == 0:
    y = sin((2 * x * x * x) - x) + (x * x)
else:
    y = (tan((x * x * x) - 3)) / 5 * log(x)

print(y)
             
