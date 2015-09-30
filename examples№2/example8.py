#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sin, exp, log

x = float(input("x? "))

if x <= -3:
    y = sin(x * x)
elif -3 < x < 5:
    y = 1 + exp(-x)
elif x < 5: 
    y = (log(x * x)) / 3 + (4 * x)

print(y)
