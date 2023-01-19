# -*- coding: utf-8 -*-
"""
Vamos a trabajar con variables y a ver diferentes ejemplos de
programacion con los mismos.

Created on Fri Jun 25 12:38:16 2021

@author: Pedro
"""

x=4 #Es una variable tipo int
y="Yep" #Es una variable tipo str

print(x)
print(y)
print("----------------------------------------------------")


"""
Vamos a cambiar los valores para acceder a nuestra variable x
como veremos ésta toma el valor de la última asignacion.
"""

x=5
x="Jupity"

print(x)
print("----------------------------------------------------")


"""
Si quieres puede especificar las variables para poder trabajar
con ella más facil mente
"""

x=str(3) #Sera una variable de tipo str
y=int(3) #Sera una variable de tipo int
z=float(3) #Sera una variable de tipo float

print(x,y,z) 
print("----------------------------------------------------")
"""
Tambien tienes que tener en cuenta que Phyton es un leguaje
case sensitive por lo cual la variable "a" sera distinta a
la variable "A".
Ademas las variables string se pueden asignar con "" o con ''.
"""
x="Serpiente"
y='silofono'
a=int (2)
A=int (2)

print("Así quedaria la revision "+x,y,A,a )
print("----------------------------------------------------")
 
"""
Tiene la propiedad de axadir varias variables.
"""

x,y,z = "Rojo","Azul","Verde"

print(x)
print(y)
print(z)
print("----------------------------------------------------") 

"""
Tiene la propiedad de que si tenemos variables en una lista,
podemos asignarle variables, por la propiedad de "Unpack".
"""

cafes =["moca","expreso","capuchino"]
x,y,z = cafes
print(x)
print(y)
print(z)
print("----------------------------------------------------") 

"""
vamos a ver como combinamos variabes.
No se pueden sumar dos variables de distinto tipo!!!
En nuestro ejemplo nooooo podemos hacer x+z
"""
x=2
y=5
z="cafe "
f="maquiato "

g= x+y
h= z+f
print(g)
print(h)
print(x+y)
print(z+f)
print("----------------------------------------------------")

"""
Como trabajan las variables en las funciones
Solo operan dentro de las funciones.
"""

x="primavera"

def myfunc():
    x="otoño"
    
    print("Esta estacion es "+x)

myfunc()
print("Sinembargo es "+x)
print("----------------------------------------------------")

"""
Tambien se puede asignar la variable con la caracteristica global
para que tb se pueda operar con ella fuera de la funcion
"""

x="primavera"

def myfunc():
    global x
    x="otoño"
        
    
    print("Esta estacion es "+x)

myfunc()
print("Sinembargo es "+x)
print("----------------------------------------------------")
