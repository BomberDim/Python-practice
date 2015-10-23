#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Введите число "))
N = int

if 1 <= n <= 250:
    N = n * 7
    print(N)
elif 251 <= n <= 299:
    N = n * 17
    print(N)
elif n >= 300:
    N = n * 20
    print(N)
else:
    print("Вы не ввели число")

    
