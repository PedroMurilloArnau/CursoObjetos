# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:47:15 2023

Analisis exploratory y visualizacion grafica

instalamos la libreria de scipy

    pip install scipy


@author: Pedro
"""

import ModuloDatos as md
import matplotlib.pyplot as plt

ruta = 'F:\\DAW\\datos\\'

fichero = 'precios_coches.csv'

#Agregacion de datos

datos = md.cargarDatos(ruta,fichero,',')
print(datos.head())

#Columna indice

datos.set_index('Unnamed: 0', inplace=True)
datos.index.name = "indice"
print(datos.head())

#Cambio nombre columnas

print(md.dameColumnas(datos))
titulos_cabecera = ['nombre','localizacion','año','kilometrosRecorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio']
md.cambiaColumnas(datos,titulos_cabecera)
print(md.dameColumnas(datos))

#Esatdisticos basicos

print(md.dameEstadisticos(datos))
print("*"*100)
print(md.dameEstadisticos(datos,"numericos"))
print("*"*100)

#Valores nulos

datos = md.reemplazarNulos(datos,'asientos')
print(md.dameEstadisticos(datos))

#cambio de tipo

datos['potencia'] = md.cambiaTipo(datos['potencia'])
datos = md.reemplazarNulos(datos,'potencia')

print(datos['motor'])
print(datos['potencia'])
print(datos.info)
print(datos['nombre'].value_counts())
print("*"*100)
print(datos['año'].value_counts())


datos['precio'] = md.cambiaTipo(datos['precio'])
datos = md.reemplazarNulos(datos,'precio')
print(datos['precio'].head())

#visualizacion

plt.boxplot(datos['precio'])
plt.title('precio')
plt.show()

#Graficas de dispersion

y = datos['precio']
x = datos['potencia']
plt.scatter(x,y)
plt.title('Potencia ; Precio')
plt.ylabel('Precio')
plt.xlabel('Potencia')
plt.show()

x = datos['motor']
plt.scatter(x,y)
plt.title('Motor ; Precio')
plt.ylabel('Precio')
plt.xlabel('Motor')
plt.show()



#obtener unos datos dependiendo del coeficioente de correlaccion  y p valor
# 
# 
# 
# p valor cerca del coefieciente de coorrelaccion certeza en el result

datos = md.reemplazarNulos(datos,'motor')

from scipy import stats
pearson_coef, p_valor = stats.pearsonr(datos['motor'], datos['precio'])
print(f"El Coeficiente de correlacion de Pearson es : {pearson_coef}")
print(f"El p valor es : {p_valor}")
