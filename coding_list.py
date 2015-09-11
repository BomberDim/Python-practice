#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import encodings

als = encodings.aliases.aliases

for key, value in als.items():
    print("{0} => {1}".format(key, value))
