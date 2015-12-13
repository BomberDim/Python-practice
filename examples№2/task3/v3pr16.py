#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a >= 0 and a <= 1:
    print(a)
if b >= 0 and b <= 1:
    print(b)
if c >= 0 and c <= 1:
    print(c)
else:
    print("Числа не входят в диапазон (0, 1)")
