#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, sqrt, cos

a, b, x = 0.7, 0.05, 0.5
t = sin(x + a)
w = (x + b)
c = cos(w * w * w)

z = (x * x * (x + 1)) / (b - (t * t))
s = sqrt((x * b) / a) + (c * c)

print(z)
print(s)
