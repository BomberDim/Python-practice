#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))

if x1 == x2 and y1 == -y2:
    print("Точки симметричны оси Ох")
elif x1 == -x2 and y1 == y2:
    print("Точки симметричны оси Оy")
else:
    print("Точки не ссиметричны") 
