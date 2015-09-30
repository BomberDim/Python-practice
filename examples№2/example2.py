#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, log

x = float(input("x? "))
a = 2.3
z = (x - 2)
c = cos(x)

if x < 1:
    y = 1.5 * (c * c)
elif x == 1:
    y = 1.8 * a * x
else:
    y = (z * z) + a

print(y)
