#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    name = input("Введите ваше имя: ")
    print("Привет,", name)
    
except EOFError:
    print(" ")  #Зачем вообще нужна и необходима ли обработка данного исключения?
    
input("Нажмите <Enter> для закрытия окна")




    
    
