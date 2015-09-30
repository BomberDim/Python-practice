#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, cos, pi, sin, tan, exp

x, y, z, = 1.426, -0.823, 2.724
s = sin(x + y)

a = (sqrt(x) + (2 * cos(x + (pi / 6)))) / 2.4 - (s * s)
b = 1.8 + (exp(-y * z) / 1 + tan(x + y + z))

print(a)
print(b)
