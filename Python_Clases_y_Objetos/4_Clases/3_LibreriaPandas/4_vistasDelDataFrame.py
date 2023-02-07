import pandas as pd
import numpy as np

"""
    1. Vamos a realizar vistas de nuestro dataFrame
    Donde crearemos las vistas a traves de condiciones

    2. Eliminamos los valores nulos

    3. Podemos hacer uniones de dataFrames

    4. Elementos unicos

    5. Veces que se repite

    6. Aplicar una multiplicacion a todos los valores

    7. Ordenar los articulos

    8. Estadisticas de nuestros valores

    9. Pasar el DataFrame a un archivo csv

"""

filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columnas = ['articulo1','articulo2','articulo3','articulo4']

datos = [[124,np.NAN,200,25],[200,100,np.NAN,34],[300,100,400,np.NAN],[300,100,500,75]]

dataFrame = pd.DataFrame(datos,index=filas,columns=columnas)
print(dataFrame)

#Le asignamos una primera condicon
condicion = dataFrame > 200

print(dataFrame[condicion])

#Podemos incluir varias condiciones
condicion = (dataFrame['articulo1'] ==200) | (dataFrame['articulo3'] <= 300)

print(dataFrame[condicion])

condicion = (dataFrame['articulo1'] ==200) & (dataFrame['articulo3'] <= 300)

print(dataFrame[condicion])

# Vamos a crear una nueva columna de indices como referencia
nuevaColumna = '1 2 3 4'.split()
dataFrame['indices'] = nuevaColumna
print(dataFrame)

dataFrame = dataFrame.set_index('indices')
print(dataFrame)

### Vamos a eliminiar los valores nulos ###

# dataFrame.dropna(axis=1,inplace=True) # De esta forma borrariamos las columnas no nan
# dataFrame.fillna(value=0, inplace=True) # De esta forma le asignamos 1 valor a los na
media = dataFrame.mean()
print(f"La media sera igual a {media}")
dataFrame.fillna(value=media, inplace=True)
print(dataFrame)

### Vamos a ver uniones de dataframes por filas con axis = 0o sin rellenar###
data1 = dataFrame.copy()
data2 = dataFrame.copy()

dataTotal = pd.concat([data1,data2], axis = 0)
print(dataTotal)

### Podemos ver los articulos unicos de una columna mediante .uniq ###
print(f"Podemos ver los articulos1 unicos: {dataFrame['articulo1'].unique()}")

### Veces que se repite por columna mediante value counts
print(f"Podemos ver las veces que se repiten: {dataFrame['articulo2'].value_counts()} ")

### Le aplicamos una multiplicacion a todos los valores ###
dataTotal = dataTotal.apply(lambda x: x*3)
print(dataTotal)

### Podemos ver las columnas mediante .columns e indices ###
print(dataTotal.columns)
print(dataTotal.index)

### Podemos ordenar los articulos mediante la funcion sort_values ###
print(dataTotal.sort_values(['articulo3']))

### Podemos ver las estadisticas de nuestro dataFrame ###
print(dataTotal.describe())

### Podemos crear una archivo csv ###
dataTotal.to_csv('dataTotal.csv')
dataFrame = pd.read_csv('dataTotal.csv', index_col=0)
print(dataFrame)