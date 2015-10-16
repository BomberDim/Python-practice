#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mounth = input("Введите название месяца ")

if mounth == "январь":
    print("В январе 31 день")
elif mounth == "февраль":
    print("Если год високосный - 28 дней, если обычный год - 29 дней")
elif mounth == "март":
    print("В марте 31 день")
elif mounth == "апрель":
    print("В апреле 30 дней")
elif mounth == "май":
    print("В мае 31 день")
elif mounth == "июнь":
    print("В июне 30 дней")
elif mounth == "июль":
    print("В июле 31 день")
elif mounth == "август":
    print("В августе 31 день")
elif mounth == "сентябрь":
    print("В сентябре 30 дней")
elif mounth == "октябрь":
    print("В октябре 31 день")
elif mounth == "Ноябрь":
    print("В ноябре 30 дней")
elif mounth == "декабрь":
    print("В декабре 31 день")
else:
    print("Вы не указали месяц")
    
