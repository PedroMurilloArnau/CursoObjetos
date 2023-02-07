import pandas as pd
import numpy as np

"""
Primero comprobamos que tenemos instalado la libreria

    pip install pandas

Luego importamos la libreria

"""

etiquetas = ['a','b','c','d','e']
datos = np.arange(4,9)
serie = pd.Series(datos, index=etiquetas)
print(serie)

# Acceder a un valor de la serie
print(serie['c'])

# Podemos agregar datos de distinto tipo
# Si no creamos etiquetas nos las asigna numericamente

datos = ['Pedro',45,'Mar',5]
serie = pd.Series(datos)
print(serie)
print(serie[0]) # De esta forma sacamos el correspondiente a la etiqueta 0

#Podemos darle datos directos

serie = pd.Series([1000,500,1200,700],["Emp01","Emp02","Emp03","Emp04"])
print(serie)