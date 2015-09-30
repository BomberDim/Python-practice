#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, exp, tan

x = float(input("x? "))
a, b = 2.574, -0.418

if x < 2.8:
    y = exp(-1.2 * x) + (b * tan(x))
elif 2.8 <= x < 6:
    y = (x + 2) / (a + b)
else:
    y = cos(x) + exp(2 * x)

print(y)
