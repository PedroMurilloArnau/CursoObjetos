# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:45:52 2023

Metodos basicos

    1- Como ver los datos de nuestro dataset
    2- Procesamientos de datos
@author: Pedros
"""

import pandas as pd
import numpy as np

fichero = 'F:\DAW\datos\precios_coches.csv'

df = pd.read_csv(fichero)


#Mediante dtypes nos muestra el tipo de dato a mostrar
print(df.dtypes)


#Con datos estadisticos de las variables numericas
print(df.describe())


#De la asiguiente manera nos mostraría tb los que no son numeros
print(df.describe(include='all'))

print(df.info())


### Procesamientos de datos ###

#Vamos a ver 1 columna
print(df['Seats'].head(5))

# df['Seats'] = df['Seats']+1 #Cambiamos los valores de nuestra columna

print(df['Seats'].head(5))

#sustituir valores faltantes

#df.dropna(subset=['Seats'],axis=0,inplace=True) #Podemos borrrar los registros
#print(df.info()) #Como vemos se implemento correctamente

#df.replace(np.nan,'nulo') #Podemos reemplazarlo por un valor
#print(df['Seats'] > 4)


#Podemos sustituir valores por la media
print(df['Seats'].describe())
media_asientos = df['Seats'].mean()
print(f"Reemplazamos por la media que seria {media_asientos}")
df['Seats'].replace(np.nan,media_asientos,inplace=True)
print(df['Seats'].describe())


