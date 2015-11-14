#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = (b * b) - (4 * a * c)

if a == 0:
    print("Ошибка, a < 0")
if D > 0:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print("x1 = ", x1, "x2 =", x2)
elif D == 0:
    x1 = (-b / (2 * a))
    print("x1 =", x1)
else:
    D < 0
    print("Нет действительных корней")

