#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, sin, exp, cos

x = float(input("x? "))
a = 2.573

if x > a:
    y = x * sqrt(x - a)
elif x == a:
    y = x * sin(x * a)
else:
    y = exp(-a * x) * cos(a * x)

print(y)
