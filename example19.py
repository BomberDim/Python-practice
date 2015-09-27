#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, sin, sqrt, cos, exp

a, b, x = 3.2, 17.5, -4.8
t = tan(x)

y = (b * (t * t)) - (a / sin(x / a))
d = a * exp(-sqrt(a)) * cos((b * x) / a)

print(y)
print(d)

