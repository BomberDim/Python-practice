#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import atan, log

x = float(input("x? "))
l = log((x * x) + 1)

if x <= -3:
    y = l * l * l
elif x > 3:
    y = atan(1 / (2 * x) + 1)

print(y)
