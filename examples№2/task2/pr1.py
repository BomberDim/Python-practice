#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input("Укажите Ваш возраст: "))

if n < 1:
    print("Вы еще не родились")
elif n > 100:
    print("Вы еще не мертвы?")
elif n == 11:
    print("Вам", n, "лет")
elif n == 12:
    print("Вам", n, "лет")
elif n == 13:
    print("Вам", n, "лет")
elif n == 14:
    print("Вам", n, "лет")
elif n % 10 == 1:
    print("Вам", n, "год")
elif n % 10 == 2:
    print("Вам", n, "года")
elif n % 10 == 3:
    print("Вам", n, "года")
elif n % 10 == 4:
    print("Вам", n, "года")
else:
    print("Вам", n, "лет")
    

    
    
