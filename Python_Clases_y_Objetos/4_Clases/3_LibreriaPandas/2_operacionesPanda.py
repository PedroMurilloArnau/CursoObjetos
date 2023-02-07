import pandas as pd
import numpy as np

"""
Principales operaciones de pandas

"""

# Operaciones de suma

serie1 = pd.Series([1000,500,1200,700],["Emp01","Emp02","Emp03","Emp04"])
print(serie1)

serie2 = pd.Series([10065,590,9850,980],["Emp01","Emp02","Emp03","Emp04"])
print(serie2)

serie3 = serie1 + serie2 #Podemos sumar dos series de indices iguales
print(serie3)