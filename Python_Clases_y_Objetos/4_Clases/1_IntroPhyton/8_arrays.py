# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:42:03 2023

Array list

@author: Usuario
"""

#Vamos a trabajar con las listas


lista = []

print(lista)

lista = [1,2,3,4]

print(lista)

#Podemos añadirle un valor mediante append

lista.append(5)

print(lista)

#Podemos borrar el ultimo elemento de la lista

borrado = lista.pop()


print(lista)
print("Borrado el numero : " + str(borrado))

borrado = lista[1]

lista.remove(2)

print(lista)
print("Borrado el numero : " + str(borrado))

