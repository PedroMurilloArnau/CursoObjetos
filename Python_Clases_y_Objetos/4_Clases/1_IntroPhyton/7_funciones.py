# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:30:51 2023

Funciones

@author: Usuario
"""

#Para definir una funcion utilizamos el nombre reservado def

def suma(num1,num2):
    total = num1 + num2
    
#Podemos mostrarlo y devolverlo

    print(total)
    return total

total = suma(1,2)
print(total)

num3 = int(input("Introduce el primer termino : "))
num4 = int(input("Introduce el segundo termino : "))

total = suma(num3,num4)
print(total * 2)