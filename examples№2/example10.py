#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, exp, cos

x = float(input("x? "))

if x < 1:
    y = ((5 * x) + 9)**1/3
elif x <= x < 4:
    y = (x * x) / 6 + exp(-x)
else:
    y = cos((3 * (x * x * x)) + 8)

print(y)
