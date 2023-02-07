import pandas as pd
import numpy as np

"""
Utilizacion de dataframes de datos
ordenados por filas y columnas
    1- index = filas
    2- columns = columnas de datos

"""

filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columnas = ['articulo1','articulo2','articulo3',]

datos = [[124,100,200],[200,100,300],[300,100,400],[400,100,500]]


# Para crear los data Frames se crearian de la siguiente forma
dataFrame = pd.DataFrame(datos,index=filas,columns=columnas)
print(dataFrame)

# Para extraer una fila
print(dataFrame.loc['tienda2'])

# Podemos sacar n filas
print(dataFrame.loc[['tienda1','tienda3']])

# Podemos extraer una columnas
print(dataFrame['articulo3'])

# Para mostrar un valor concreto
print(dataFrame.loc['tienda2','articulo3'])

# Podemos añadir una nueva columna
dataFrame['articulo4'] = 25
print(dataFrame)

#Podemos extraer una suma de todas las columnas
dataFrame['total'] = dataFrame['articulo4'] + dataFrame['articulo3'] + \
    dataFrame['articulo2'] + dataFrame['articulo1']
print(dataFrame)

#Podemos eliminar una columna mediante axis ojo!
# dataFrame = dataFrame.drop(['total'],axis=1) Una forma valida
print(dataFrame.drop(['total'],axis=1, inplace=True)) #el borrado se queda en el dataFrame
print(dataFrame)

