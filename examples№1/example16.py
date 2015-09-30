#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, fabs, exp, sin, cos

a, b, t = 1.5, 15.6, 0.9

v = sqrt(fabs((b * t) - a)) - (exp(sqrt(b * t)) * sin((b * t) + a))
z = 1 + (b * sin((a * (t * t)) * cos(3 * t)))

print(v)
print(z)
