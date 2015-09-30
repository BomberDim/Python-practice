#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, exp

x = float(input("x? "))

if x < -2:
    y = (2 + cos((x * x * x) + 3)) / 4 + (x * x)
elif -2 <= x < 3:
    y = 2 - exp(2 * x)
else:
    y = cos((x * x) + (5 * x)) / ((5 * x * x) - 2)

print(y)
