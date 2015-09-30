#!/bin/usr/env python3
# -*- coding: utf-8 -*-

from math import sqrt, fabs

x = 1.825
y = 18.225
z = -3.289

s = fabs(x**(y/x) - ((y/x)**1/3))
t = (y - x) * (y - (z *(y - x)))/1 + (y - x)**2

print("s =", s)
print("t =", t)
