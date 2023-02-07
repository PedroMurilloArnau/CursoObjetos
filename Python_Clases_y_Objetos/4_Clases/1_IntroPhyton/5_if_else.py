# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:05:43 2023

If Else

@author: Pedro
"""

#Para trabajar con if else debemos de acompañarlos de :

n = int(input("Adivina el numero : "))

if n == 15 :
    print("Acertaste")
    print("todo")
else:
    print("Fallaste")
    
#Tambien podemos utilizar un ilef

if n == 15 :
    print("Acertaste")
elif ( abs(15 - n) <= 5):
    print("Calinete caliente")
else:
    print("Estas muy alejado")