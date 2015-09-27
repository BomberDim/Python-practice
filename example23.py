#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, sqrt, exp, log

a, b, x = 0.3, 0.9, 0.61

y = exp((2 * x) * log(a)) + (exp((-x) * log(b)) * cos(a + b) * x)
k = exp(a * x) / sqrt(2) * cos(sqrt((b * x) / 2))

print(y)
print(k)
