#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, exp

x = float(input("x? "))
s = sin((5 * x * x) + (3 * x) + 1)

if x < -2.5:
    y = s * s * s * s * s
elif -2.5 <= x < 4:
    y = x * sin((4 * x) - 1)
else:
    y = exp(-6 * x) + 8

print(y)
