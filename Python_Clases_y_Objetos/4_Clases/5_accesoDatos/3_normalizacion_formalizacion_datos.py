# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:30:18 2023

Normalizacion de datos

    1- Cambiar el tipo de datos
    2- Como normalizar los datos

@author: Pedro
"""

import pandas as pd
import numpy as np

fichero = 'F:\DAW\datos\precios_coches.csv'

df = pd.read_csv(fichero)
print(df.head())

print(df.dtypes)

#Podemos cambiar el tipo de dato

df['Unnamed: 0'] = df['Unnamed: 0'].astype('float64')
print(df.dtypes)

#Hacer calculos y ponerlos a otra columna

# millas = kilometros*0,621371
df['millas_driven'] = df['Kilometers_Driven']*0.621371
print(df.dtypes)

#De la siguiente manera podemos renombrar las columnas
df.rename(columns={'millas_driven':'Millas'},inplace=True)
print(df.dtypes)

### Normalizar los datos ###

# Escalado minimo y valor anterior
print(df[['Millas','Kilometers_Driven']])
df['Millas_normalizada'] = df['Millas']/df['Millas'].max()
df['Kilometros_normalizada'] = df['Kilometers_Driven']/df['Kilometers_Driven'].max()
print(df[['Kilometros_normalizada','Millas_normalizada']])

#tomando el minimo y el maximo
df['Millas_normalizada'] = (df['Millas']-df['Millas'].min())/(df['Millas'].max()-df['Millas'].min())
df['Kilometros_normalizada'] = (df['Kilometers_Driven']-df['Kilometers_Driven'].min())/(df['Kilometers_Driven'].max()-df['Kilometers_Driven'].min())
print(df[['Kilometros_normalizada','Millas_normalizada']])



