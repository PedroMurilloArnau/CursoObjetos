# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:51:41 2023

Variables

@author: Usuario
"""

#Como variables podemos no asignarles valores

precio = 20
cantidad = 2
total = precio + cantidad

print(total) 

#Para trabajar con string

texto1 = "hola"
texto2 = " buenos dias"

total = texto1 + texto2

print(total)

#Podemos ver la longitud de nuestra cadena con len

print(len(total))

#Mostraremos nuestra de nuestra cadena del caracter 2 mendiante

print(total[2])

#O mostrar un trozo de nuestra cadena

print(total[5:16])

#Entrada y salida

#Utilizamos el metodo strip() para quitar los espacios!

nombre = input("Dime tu nombre: ").strip()
edad = int(input("Dime tu edad : "))

print("Hola " + nombre + " tienes " + str(edad) + " años.")