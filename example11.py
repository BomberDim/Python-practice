#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, sqrt, exp

a, b, x = 16.5, 3.4, 0.61
v = (x + b)

s = (x * x * x) * tan(v * v) + (a / sqrt(v))
d = ((b * (x * x)) - a) / (exp(a * x) - 1)

print(s)
print(d)
