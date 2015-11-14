#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

from math import fabs

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if fabs(a) >= 4 and fabs(b) >= 4 and fabs(c) >= 4:
    print(a, b, c)
elif fabs(a) < 4 and fabs(b)>= 4 and fabs(c) >= 4:
    print(b, c)
elif fabs(b) < 4 and fabs(a)>= 4 and fabs(c) >= 4:
    print(a, c)
elif fabs(c) < 4 and fabs(a)>= 4 and fabs(b) >= 4:
    print(a, b)
elif fabs(a) < 4 and fabs(b) < 4 and fabs(c) >= 4:
    print(c)
elif fabs(a) < 4 and fabs(c) < 4 and fabs(b) >= 4:
    print(b)
elif fabs(b) < 4 and fabs(c) < 4 and fabs(a) >= 4:
    print(a)
else:
    print("Число не соотвествует условию |a, b, c|")
