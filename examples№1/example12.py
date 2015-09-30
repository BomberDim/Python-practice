#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, sqrt, exp

x, a, b = 0.54, 1.1, -1.22
d = (x + (a * a))
c = cos(d * d)
t = (x + b)

y = (c * c) + sqrt(x / (b * b))
z = ((a * a) / (x * x)) + exp(t * t *t)

print(y)
print(z)
