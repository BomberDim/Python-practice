#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and x % y == 0:
    print("Число делится без остатка")
elif x > 0 and x % y != 0:
    print("Число делится с остатком")
