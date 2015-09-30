#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs, sin, tan, exp, log

x, y, z = 1.82, 18.23, 3.44
w = (x - y)

s = fabs(exp((y / x) * log(x)) - (x / y)**1/5)
t = (x - y) * (sin(x + y) - (tan(y - x) * z) / 1 + (w * w))

print(s)
print(t)
