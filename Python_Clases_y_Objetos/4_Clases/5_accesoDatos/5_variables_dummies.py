# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:45:33 2023

Variables dummies

@author: Pedro
"""



import pandas as pd

fichero = 'F:\DAW\datos\precios_coches.csv'

df = pd.read_csv(fichero)

print(df.columns)
print(df['Fuel_Type'])

#Vamos a crear variable categorica con el tipo de Fuel

columna_dummies = pd.get_dummies(df['Fuel_Type'])
print(columna_dummies)

df_dumies = pd.get_dummies(df,columns=['Fuel_Type'])
print(df.head)
print('*'*25)
print('*'*25)
print(df_dumies.head)

'''

Un ejemplo de variable Dummie sería la que nos valoran un datos de Estado

ESTADO
bueno 1
malo  0
regular 2

La columna regular la podriamos quitar dado q podriamos expresar comoo 00
ESTADO bueno malo 
        1       0       
        0       1       
        0       0       
'''