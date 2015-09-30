#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, sqrt, exp

x = float(input("x? "))
s = sin(x)

if x < 1:
    y = x * s * s
elif x == 1:
    y = sqrt((x * x * x * x * x) + 15)
else:
    y = exp(x)

print(y)

