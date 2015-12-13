#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))

if fabs(x1) == fabs(x2) and fabs(y1) == fabs(y2):
    print("Точки симметричны")
else:
    print("Точки не симметричны")
