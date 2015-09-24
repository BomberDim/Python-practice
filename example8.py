#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import exp, fabs, log, sqrt 

x, m, c = 0.9, 1.2, 2.4
y = float(input("Введите значение y = "))

a = exp(-m * x) * sqrt(m + (x * x)) / (fabs((m * m) - (x * x)))
b = log(c * c + sqrt(c + y)) + exp(-c * y)

print(a)
print(b)
