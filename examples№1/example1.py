#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import cos, pi

x = 1.426
y = -1.220
z = 3.5

a = 2 * cos(x - pi/6)/0.5 + ((1 - cos(2*y))/2)

b = 1 + (2 / (3 + (z**2/5)))

print("a =", a)

print("b =", b)

input()
