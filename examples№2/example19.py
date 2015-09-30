#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import exp, cos

x = float(input("x? "))

if x < 1:
    y = ((5 * x * x) + (9 * x))**1/3 + (3 * x)
elif 1 <= x < 4:
    y = ((x * x * x * x * x) - (2 * x * x * x * x) - 5) / ((2 * x * x * x) + exp(-x))
else:
    y = (6 * x) + cos((5 * x * x * x) + 8)

print(y)
    
