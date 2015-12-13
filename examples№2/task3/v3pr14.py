#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > b and a > c and b > c:
    print("Наибольшее", a, "Наименьшее", c)
elif b > c and b > a and c > a:
    print("Наибольшее", b, "Наименьшее", c)
elif c > a and c > b and a > b:
    print("Наибольшее", c, "Наименьшее", b)
elif c > b and c > a and b > a:
    print("Наибольшее", c, "Наименьшее", a)
elif b > a and b > c and a > c:
    print("Наибольшее", b, "Наименьшее", c)
elif a > c and a > b and c > b:
    print("Наибольшее", a, "Наименьшее", b)
else:
    print("Ошибка")
