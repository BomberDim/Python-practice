#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b*b - 4*a*c
y1 = (-b - sqrt(D))/(2*a)
y2 = (-b + sqrt(D))/(2*a)

if a == 0:
    print("Ошибка, a < 0")

if y1 >= 0 and y2 >= 0:
    x1 = sqrt(y1)
    x2 = -sqrt(y1)
    x3 = sqrt(y2)
    x4 = -sqrt(y2)
    print("x1 = ", x1, "x2 =", x2, "x3 =", x3, "x4 =", x4)
elif y1 >= 0:
    x1 = sqrt(y1)
    x2 = -sqrt(y1)
    print("x1 = ", x1, "x2 =", x2)
elif y2 >= 0:
    x1 = sqrt(y2)
    x2 = -sqrt(y2)
    print("x1 = ", x1, "x2 =", x2)
else:
    D < 0
    print("Нет действительнх корней")




