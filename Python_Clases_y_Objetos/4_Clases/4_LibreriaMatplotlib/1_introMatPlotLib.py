import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
Primero comprobamos que tenemos instalado la libreria

    pip install matplotlib

Luego importamos la libreria

Más informacion en https://matplotlib.org/

"""

x = np.linspace(1,150,200) # Creamos 200 datos entre el 1 y el 150
y = x + x**2
# print(x)
# print(y)

plt.plot(x,y,'blue') # .hist area bar pie scatter box
plt.title('Mi grafico')
plt.xlabel('Valores x')
plt.ylabel('Valores y')
plt.show()


#subplots

plt.subplot(1,2,1)
plt.plot(x,y,'g')
plt.subplot(1,2,2)
plt.plot(x,y,'r')
plt.show()