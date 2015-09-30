#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, fabs, sin, cos

m, c, t, b = 2, -1, 1.2, 0.7

a = ((m * tan(t)) + fabs(c * sin(t)))**1/3
z = (m * cos((b * t) * sin(t))) + c

print(a)
print(z)
