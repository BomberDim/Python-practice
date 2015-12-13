#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))

if a1 == 0 and b1 == 0 or a2 == 0 and b2 == 0:
    print("Прямые не существуют")
elif a1*b2 == a2*b1 and a1*c2 == a2*c1:
    print("Пряимые совпадают")
elif a1*b2 == a2*b1:
    print("Прямые параллельны")
