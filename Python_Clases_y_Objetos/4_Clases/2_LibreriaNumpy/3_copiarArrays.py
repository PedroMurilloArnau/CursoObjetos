import numpy as np

#Vamos a copiar un array

array = np.arange(1,11)
array2 = array.copy()
print(array)
print(array2)

array2[4] = 899999

print(array)
print(array2)
