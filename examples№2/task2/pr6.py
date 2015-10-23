#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import fabs
C = int(input("|C| < 9, C = "))

if fabs(C) == 1:
    print("Один")
elif fabs(C) == 2:
    print("Два")
elif fabs(C) == 3:
    print("Три")
elif fabs(C) == 4:
    print("Четыре")
elif fabs(C) == 5:
    print("Пять")
elif fabs(C) == 6:
    print("Шесть")
elif fabs(C) == 7:
    print("Семь")
elif fabs(C) == 8:
    print("Восемь")
else:
    print("Число не соответствует условию")
