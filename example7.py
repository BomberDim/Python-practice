#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, sin, exp, sqrt

a, b, t = -0.5, 1.7, 0.44

y = exp(-b * t) * sin(a * t + b) - sqrt((b * t) + a)
s = (b * sin((a * t * t) * cos(2 * t))) - 1

print(y)
print(s)
