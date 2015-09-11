# -*- coding: utf-8 -*-
import encodings.aliases
arr = encodings.aliases.aliases
keys = list(arr.key())
keys.sort()
for key in keys:
    print("%s => %s" %(key, arr[key]))


    
