#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

a, b, c = 2.8, -0.3, 4
x = float(input("x? "))

if x < 1.2:
    y = (a * (x * x)) + (b * x) + c
elif x == 1.2:
    y = (a / x) + sqrt((x * x) + 1)
else:
    y = (a + (b * x)) / sqrt((x * x) + 1)

print(y)
