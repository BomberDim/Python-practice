#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, sin, cos, exp

x = float(input("x? "))

if x > 2:
    y = (5 * x) + sqrt((x * x) + x)
elif x == 2:
    y = (9 * x) - sin((3 * x * x * x * x) - 1)
else:
    y = exp(-2 * x) + cos(2 * x)

print(y)
