#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log, exp

t = float(input("t? "))
a, b = -0.5, 2

if 1 <= t <= 2:
    y = (a * (t * t)) * log(t)
elif t < 1:
    y = 1
else:
    y = exp(a * t) + (5 *(t * t * t *t))

print(y)
