#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, log, exp, tan

x = float(input("x? "))

if x < -2:
    y = (sin(6 * x * x * x)) / ((4 * x) - (x * x * x * x))
elif -2 <= x < 3:
    y = ((2 * log(x - 1)) - exp(x)) / ((8 * x) + (x * x))
else:
    y = (((2 * x * x * x) + 4) / ((5 * x * x) - 2)) * tan((2 * x) + 1)

print(y)
