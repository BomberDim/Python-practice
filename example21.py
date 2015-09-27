#!/usr/bin/env python3
# -*- coding utf-8 -*-

from math import log, sin, exp, fabs, sqrt

a, b, x, c = 10.2, 9.2, 2.2, 0.5
s = sin(x / b)

f = log(a + (x * x)) + (s * s)
z = exp(-c * x) * ((x + sqrt(x + a)) / (x - sqrt(fabs(x - b))))

print(f)
print(z)
