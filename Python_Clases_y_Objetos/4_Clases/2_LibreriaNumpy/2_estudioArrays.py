import numpy as np

### Vamos a calcular el tamaño de un array ###

array = np.random.randint(1,201,30)
print(array)
# Vamos a crear una configuracion para los30 elementos
matriz = array.reshape(5,6)
print(matriz)

# Sacar valores máximos y minimos

array = np.random.randint(1,901,200)
print(array)
maximo = array.max()
minimo = array.min()

print(f"El valor maximo es {maximo}")
print(array.argmax())
print(f"El valor minimo es {minimo}")
print(array.argmin())

# Para mostrar elementos con sus posiciones

array = np.arange(1,11)
print(array)
print(array[2])
print(array[6:])
print(array[:8])

# 