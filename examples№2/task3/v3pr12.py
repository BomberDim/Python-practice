#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sqrt

x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
y1 = float(input("y1 = "))
y2 = float(input("y2 = "))
r1 = float(input("r1 = "))
r2 = float(input("r2 = "))

k = sqrt((x2-x1) * (x2-x1) + (y2-y1) * (y2-y1))

if k > r1+r2:
    print("Не имеют общих точек")
elif k == r1+r2:
    print("1 точка пересечения")
else:
    print("2 точки пересечения")
