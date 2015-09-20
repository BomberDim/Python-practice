#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, cos

x, y = 0.335, 0.025

s = 1 + x + (x * x / 2) + ((x * x * x) /6) + ((x * x * x * x) / 12)
t = x * (sin(x * x * x) + cos(x)**2)

print(s)
print(t)
