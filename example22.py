#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, log, fabs, exp

x, a, b, c = 3.23, 10.23, 9.84, 0.5

z = sqrt((x * x) / b) - log((a * a) + (x * x))
f = exp(-c * x) * ((x + sqrt(fabs(x - b))) / (x - sqrt(x + a)))

print(z)
print(f)
