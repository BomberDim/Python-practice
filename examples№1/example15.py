#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, sqrt, cos

x, a, b = 0.2, 1.1, 0.04
w = ((x * x) + a)
s = sin(w * w)
p = (x + b)

y = (s * s * s) - sqrt(x / b)
z = ((x * x * x) / 3) + cos(p * p * p)

print(y)
print(z)
