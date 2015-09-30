#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, exp

x = float(input("x? "))

if x < -2:
    y = cos((6 * x * x) + 3) / 4 - (x * x * x * x)
elif - 2 <= x < 3:
    y = (2 - exp(x)) / (8 + (x * x))
else:
    y = (2 * (x * x * x) + 4) / ((5 * (x * x)) - 2)

print(y)
