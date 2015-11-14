#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > b and a > c and b > c:
    print(a, b, c)
    print(c, b, a)
elif b > c and b > a and c > a:
    print(b, c, a)
    print(a, c, b)
elif c > a and c > b and a > b:
    print(c, a, b)
    print(b, a, c)
elif c > b and c > a and b > a:
    print(c, b, a)
    print(a, b, c)
elif b > a and b > c and a > c:
    print(b, a, c)
    print(c, a, b)
elif a > c and a > b and c > b:
    print(a, c, b)
    print(b, c, a)
else:
    print("Ошибка")
    
    
