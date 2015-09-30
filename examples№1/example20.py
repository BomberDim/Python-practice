#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import tan, sin, sqrt, cos, exp

a, b, x = 3.44, 17.52, 5.34
t = tan(x + a)
s = sin(a / x)

y = (a * (t * t)) - (b / (s * s))
d = b * exp(sqrt(b)) * cos(((a * x) / b) + 1.4)

print(y)
print(d)
