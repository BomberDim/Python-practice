#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

x = float(input("x? "))
a = 5

if x < 2:
    y = 6 - (x * x)
elif 2 <= x < 4:
    y = (a * math.exp(x)) / (3 + (4 * x * x * x * x * x * x))
else:
    y = (6 * (x * x * x) - (4 * x))**1/3

print(y)

