# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:17:11 2023

Bucles for, while

@author: Pedro
"""

#Un bucle for podremos recorrerlo un rango de veces o para un acondicion

for n in range(10,20,2):
    print(n)

cadena = "hola mundo";

for caracter in cadena:
    print(caracter)
    
#Bucle while podremos recorrerla mientras que no se de una condicion

nombre = input("Dime tu nombre : ").strip()

while nombre == "":
    
    nombre = input("Dime tu nombre por favor: ").strip()
print("Hola, " + nombre)
print("Bien hecho por poner tu nombre")