#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import exp, sin, log, cos

x, a, b = 0.3, 0.5, 2.9

u = a * a * x + exp(-x) * cos(b * x) / (b * x) - exp(-x) * sin(b * x) + 1
f = exp(2 * x) * log(a + x) - b**(3*x) * log(b + x)

print(u)
print(f)
