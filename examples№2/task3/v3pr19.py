#!/usr/bin/env python3
# -*- coding: utf-8

from math import sqrt

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
b1 = float(input("b1 = "))
b2 = float(input("b2 = "))

if sqrt(x1*x1 + y1*y1) > sqrt(x2*x2 + y2*y2):
    print("Точка А находится ближе")
else:
    print("Точка B находится дальше")
