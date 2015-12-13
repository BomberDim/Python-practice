#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
x3 = float(input("x3 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
y3 = float(input("y3 = "))
a = float(input("a = "))
b = float(input("b = "))

S = fabs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
S1 = fabs((x2 - x1) * (b - y1) - (a - x1) * (y2 - y1)) / 2
S2 = fabs((a - x1) * (y3 - y1) - (x3 - x1) * (b - y1))/ 2
S3 = fabs((x2 - a) * (y3 - b) - (x3 - a) * (y2 - b)) / 2

if S == S1 + S2 + S3:
    print("Данная точка принадлежит треугольнику")
else:
    print("Точка не в треугольнике")

