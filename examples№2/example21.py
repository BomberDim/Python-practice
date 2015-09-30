#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, cos, sin

x = float(input("x? "))

if x > 0:
    y = ((3 * x * x * x) * sqrt(x)) - (5 * x * x * x * x * x)
elif x == 0:
    y = cos((2 * x * x * x) - 1) + (5 * x * x * x * x * x)
else:
    y = ((3 * x * x) + sin((x * x * x) - 3)) / 5

print(y)
