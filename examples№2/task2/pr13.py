#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("Сколько кг за день собрал студент "))

if x <= 50:
    X = 0.3 * x
    print("Его заработок", X)
elif 50 < x <= 75:
    X = 0.5 * x
    print("Его заработок", X)
elif 75 < x <= 90:
    X = 0.65 * x
    print("Его заработок", X)
elif x > 90:
    X = (0.7 * x) + 20
    print("Его заработок", X)
else :
    print("Вы не ввели число")
