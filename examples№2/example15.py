#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, cos

x = float(input("x? "))

if x > 0:
    y = 2 * x * sqrt(x)
elif x == 0:
    y = cos(x * x * x * x * x) + 5
else:
    y = (x * x) / 5

print(y)
