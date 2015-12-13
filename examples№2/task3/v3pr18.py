#!/usr/bin/env python3
# -*- coding: utf-8

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b or a == c or b == c and a>0 and b>0 and c>0:
    print("Ранобедренный треугольник")
elif a == b == c and a>0 and b>0 and c>0:
    print("Равносторонний треугольник")
elif a!= b!= c and a>0 and b>0 and c>0:
    print("Разносторонний треугольник")
else:
    print("Треугольник постороить нельзя")
