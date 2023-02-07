import numpy as np

"""
 Creación de un array utilizando libreria numpy

    Mas documentacion en https://numpy.org/
    O en https://www.w3schools.com/python/numpy/default.asp

"""


lista = [1,2,3,4,5,6,3,2,1,4]
array = np.array(lista)
print(lista)
print(type(array))
print(array)

# De la siguiente manera convertimos una matriz 3x3

lista2 = [[1,2,3],[2,5,3],[9,4,2]]
array2 = np.array(lista2)
print(array2)

# Podemos rellenar un array dandole rangos de forma automatica

array = np.arange(2,25,3)
print(array)

matrizCeros = np.zeros((4,5))
print(matrizCeros)

matrizUnos = np.ones((3,4))
print(matrizUnos)

#Matriz 40 elementos con valores del 2 al 6

matriz = np.linspace(2,6,40)
print(matriz)

# Matriz identidad matriz cuadrad de n columnas y n filas en la diagonal unos

matrizIdentidad = np.eye(7)
print(matrizIdentidad)

# Matriz con numeros aleatorios 

matrizAleatoria = np.random.rand(3,4).round(1)
print(matrizAleatoria)

matrizAleatoriaNormal = np.random.randn(4,4)
print(matrizAleatoriaNormal)

matrizAleatoriaEnteros = np.random.randint(1,51,20)
print(matrizAleatoriaEnteros)

