#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, log, sin

x = float(input("x? "))
c = cos((2 * x * x) - 1)
z = ((x * x) * ((x * x * x) - (2 * x) + 5))

if x < 1:
    y = (4.8 * x * x * x * x) + (c * c)
elif x == 1:
    y = (1.8 * x) + log(4 * x)
else:
    y = (z * z) + sin((3 * x) - 1)

print(y)
