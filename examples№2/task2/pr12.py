#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x1 = int(input("Введите число x1 "))
x2 = int(input("Введите число x2 "))

if  200 <= (x1 + x2) <= 500:
    X3 = ((x1 + x2) * 3) / 100
    print(X3)
elif 500 <= (x1 + x2) <= 800:
    X3 = ((x1 + x2) * 5) / 100
    print(X3)
elif 800 <= (x1 + x2) <= 1000:
    X3 = ((x1 + x2) * 7) / 100
    print(X3)
elif (x1 + x2) > 1000:
    X3 = ((x1 + x2) * 9) / 100
    print(X3)
elif x1 + x2:
    X3 = x1 + x2
    print(X3)
else:
    print("Вы не ввели число")
    
