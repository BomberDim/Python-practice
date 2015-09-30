#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos, sqrt

a, b, x = -1.5, 15.5, -2.9
t = cos(x * x * x)

w = sqrt((x * x) + b) - b * b * sin((x + a) / x)**3
y = t * t - (x / sqrt((a * a) + (b * b)))

print(w)
print(y)
