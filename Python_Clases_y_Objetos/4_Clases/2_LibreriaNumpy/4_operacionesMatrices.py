import numpy as np

### Operaciones con matrizes ###

array = np.random.randint(1,201,30)
matriz = array.reshape(5,6)
print(matriz)

# Podemos extraer la n fila
print(matriz[0])

# Tambien podemos extraer las n primeras filas
print(matriz[:2])

# Podemos extreer por columnas
print(matriz[:,:2])

# Podemos extraer la posicion de la misma fila y de la columna determinada
print(matriz[1][2])
print(matriz[1,2])

#POdemos sacar el valor maximo y minio de una matriz

print(np.max(matriz))
print(np.min(matriz))

#Podemos sumarle o multiplicar n a cada elemento
print(matriz + 10)

#Podemos sumar o mulitplicar 2 matrices
print(matriz+matriz)

#Podemos extrar para una determinada condicion

condicion = matriz > 10 #Natriz con los numeros mayores de 10
print(matriz[condicion])

condicion = (matriz % 2 != 0) #Condicion de numeros pares
print(matriz[condicion])

#####################-----------------########################

#Valores del 5 al 40
lista = np.arange(5,41) #Creamos una nueva lista con un rango determinado
print(lista)

lista = lista.reshape(3,12) #Redimensionamos la lista a una matriz 3x12
print(lista)

print(lista[2,4]) #podemos extraer el valor de la lista del 2 al 4

#Combinacion Primitiva

arrayPrimitiva = np.random.randint(1,50,6)
print(f"El numero de la primitiv ganadora sera el {arrayPrimitiva}")





