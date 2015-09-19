#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import log, exp

a, b, c = 1.1, -2.3, 5.7
x = float(input("x? "))

y = (1 + x * (1 + x / 2 * (1 + x / 3 * (1 + x / 4 * (1 + x / 5))))) ** (1 / 5) / (c + x * (b + x * a))
z = log(b + c * x * x) * exp(-a * x) * (x ** (c * x))

print("y = {}\nz = {}".format(y, z))
