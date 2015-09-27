#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, fabs, sin, cos, exp

b, c, t = 0.7, -1.8, 1.2
m = float(input("Введите значение m = "))

f = ((m * tan(t)) + fabs(c * sin(3 * t)))**1/3
z = (m * cos((b * t) + exp(-t))) + c

print(f)
print(z)
