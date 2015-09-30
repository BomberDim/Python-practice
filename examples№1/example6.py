#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import exp, sin, log

x, a, b, c, m = 1.7, 0.5, 1.08, 2.1, 0.7

z = (sin(x) / ((1 + ((m * m) * sin(x)**2)))**1/2) - c * m * log(m * x)
s = exp(-a * x) * ((x + 1)**1/2) + exp(-b * x) * (x + 1.5)**1/2

print(z)
print(s)
