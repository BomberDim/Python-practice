#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, exp

x = float(input("x? "))
a = 0.361
s = sin((2 * x) + 1)

if x < -2.5:
    y = a * s * s
elif -2.5 <= x < 4:
    y = x * sin(x * a)
else:
    y = exp(x)

print(y)
