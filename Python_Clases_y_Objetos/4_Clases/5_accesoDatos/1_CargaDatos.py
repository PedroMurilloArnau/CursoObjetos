# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:40:56 2023

El dataset lo extraemos de kaggle https://www.kaggle.com/

Utilizando "Used Car Price Prediction" como dataset

@author: Usuario
"""

import pandas as pd

fichero = r"C:\Users\pedro\OneDrive\Documents\Datos\train-data.csv"

#datos = pd.read_csv(fichero, header=None) #si queremos que las cabeceras dentro del doc
datos = pd.read_csv(fichero)

#print(datos)
print(datos.head(5))
print("*"*10)
print(datos.tail(6))

print(datos.columns)

titulos_cabecera = ['indice','nombre','localizacion','año','kilometrosRecorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio','nuevo precio']

datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)

#Exportar datos a distintos formatos
datos.to_csv(r"C:\Users\pedro\OneDrive\Documents\Datos\precios_coches_nuevo.csv")

datos.to_json(r"C:\Users\pedro\OneDrive\Documents\Datos\precios_coches_nuevo.json")

datos.to_excel(r"C:\Users\pedro\OneDrive\Documents\Datos\precios_coches_nuevo.xlsx")

df_xcel = pd.read_excel(r"C:\Users\pedro\OneDrive\Documents\Datos\precios_coches_nuevo.xlsx")
df_json = pd.read_json(r"C:\Users\pedro\OneDrive\Documents\Datos\precios_coches_nuevo.json")


print(df_xcel.head(5))
print("*"*10)
print(df_json.head(5))
print("*"*10)

