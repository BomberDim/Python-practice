#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, sin, exp, log

x, y, b, m = 5.2, 1.9, 3.5, 0.2
t = sin(x + b)

z = x * x * x * (t * t) + (x / (x + (b * b)))
s = ((m * m) + (y * y)) * exp(m * y) + sqrt(3 * m + log(m + (4 * y))) 

print(z)
print(s)
