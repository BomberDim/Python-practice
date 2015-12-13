#!/usr/bin/env python3
# -*- coding: utf-8 -*-

year = int(input("Введите год: "))

color = (year % 10)
animal = ((year - 1984) % 12)

if color == 0 or color == 1:
    color = "Год бело"
elif color == 2 or color == 3:
    color = "Год черно"
elif color == 4 or color == 5:
    color = "Год зелено"
elif color == 6 or color == 7:
    color = "Год красно"
elif color == 8 or color == 9:
    color = "Год желто"
else:
    print("Год не соотвсетствует значению")

if animal == 0:
    animal = "й мыши"
    print(color + animal)
elif animal == 1:
    animal = "й коровы"
    print(color + animal)
elif animal == 2:
    animal = "го тигра"
    print(color + animal)
elif animal == 3:
    animal = "го зайца"
    print(color + animal)
elif animal == 4:
    animal = "го дракона"
    print(color + animal)
elif animal == 5:
    animal = "й змеи"
    print(color + animal)
elif animal == 6:
    animal = "й лошади"
    print(color + animal)
elif animal == 7:
    animal = "й овцы"
    print(color + animal)
elif animal == 8:
    animal = "й обезьяны"
    print(color + animal)
elif animal == 9:
    animal = "й курицы"
    print(color + animal)
elif animal == 10:
    animal = "й собаки"
    print(color + animal)
elif animal == 11:
    animal = "й свиньи"
    print(color + animal)
else:
    print("Год не соответсвует значению")
