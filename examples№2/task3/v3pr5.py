#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = float(input("x = "))
y = float(input("y = "))

a = (x * x) + (y * y)
b = (x * x) + (y * y)

if a == 1 and b == 0.25:
    print("Точка А принадлежит окружности")
else:
    print("Точка А не принаджежит окружности")
