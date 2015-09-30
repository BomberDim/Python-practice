#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import pi, sqrt, log

x = float(input("x? "))
a = 1.3

if x < 1.3:
    y = (pi * (x * x)) - (7 / (x * x))
    
elif x == 1.3:
    y = (a * (x * x * x)) - (7 * sqrt(x))
    
else:
    y = log(x + (7 * sqrt(x)))

print(y)
