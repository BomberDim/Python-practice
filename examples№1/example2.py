#!/bin/usr/env python3
# -*- coding: utf-8 -*-

from math import sqrt, exp, sin, fabs

x = 1.4

a = 0.5

b = 3.1

z = sqrt(a * x * sin(2*x)) + (exp(-2*x)*(x+b))
w = exp(3 * fabs(sin(b * x))) - ((x**3)/a)

print("z =", z)
print("w =", w)

input()
