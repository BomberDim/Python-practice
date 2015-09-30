#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos

x, y = 0.335, 0.025

s = 1 + x * (1 + x / 2 * (1 + x / 3 * (1 + x / 4)))
t = x * (sin(x * x * x) + cos(x)**2)

print(s)
print(t)
