#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
r = float(input("r = "))

if r*r >= a1*a1 + a2*a2:
    print("Точка А принадлежит окружности")
else:
    print("Точка А не принадлежит окружности")
