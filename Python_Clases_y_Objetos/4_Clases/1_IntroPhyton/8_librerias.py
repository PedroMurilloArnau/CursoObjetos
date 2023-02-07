# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 12:01:32 2023

Diccionarios

@author: Usuario
"""

#A continuacion vamos a trabajar con diccionarios

meses={'Enero':1,'Febrero':2,'Marzo':3}
print(meses)
print(meses['Febrero'])
meses['Abril'] = 4
print(meses)

del meses["Enero"]
print(meses)

for clave, valor in meses.items():
    print(clave+" es el mes "+str(valor))