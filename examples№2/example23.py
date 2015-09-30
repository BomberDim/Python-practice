#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, tan, log, exp

x = float(input("x? "))

if x < 1:
    y = ((5 * x * x) + sin(x) - x)**1/6 + (3 * x)
elif 1 <= x < 4:
    y = (cos(x) - (x * x * x * x * x) - 5) / ((2 * x * x * x * x * x) + exp((-2 * x) - 1))
else:
    y = (6 * tan(2 * x)) + log((5 * x * x * x) + 8)

print(y)
                                                                        
