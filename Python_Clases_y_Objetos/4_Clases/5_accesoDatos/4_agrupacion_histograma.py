# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 22:45:13 2023

Agrupacion e histograma

    1- Agrupacion
    2- Histograma

@author: Pedro
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fichero = 'F:\DAW\datos\precios_coches.csv'

df = pd.read_csv(fichero)

print(df.columns)

titulos_cabecera = ['indice','nombre','localizacion','año',
                    'kilometrosRecorridos','combustible','transmision',
                    'tipo propietario','kilometraje','motor','potencia',
                    'asientos','precio']

df.columns = titulos_cabecera
print(df.columns)

### Agrupacion ###
#Podemos hacer una agrupacion por un intervalo de n

intervalo = np.linspace(min(df['kilometrosRecorridos']),
                        max(df['kilometrosRecorridos']),4)
print(intervalo)
nombre_grupos = ['pocos','normal','muchos']
df['kilometrosAgrupados']=pd.cut(df['kilometrosRecorridos'], intervalo, 
                                 labels=nombre_grupos, include_lowest=True)
print(df['kilometrosAgrupados'])

### Histograma ###
#Vamos a crear un histograma con nuestros datos

plt.hist(df['kilometrosRecorridos'],bins=intervalo, rwidth=0.9, color = '#991')
plt.title('Histograma de Kilometros recorridos')
plt.xlabel('Kilometros')
plt.ylabel('Frecuencia')
plt.show()
