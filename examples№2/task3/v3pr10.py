#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
elif c > a and c > b:
    print(c)
elif a == b and a == c:
    print(a)
else:
    print("Ошибка")
    
