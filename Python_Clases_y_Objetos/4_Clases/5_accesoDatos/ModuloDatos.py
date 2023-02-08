import pandas as pd
import numpy as np


def cargarDatos(ruta,fichero):
    df = pd.read_csv(ruta + fichero)
    return df

def dameColumnas(df):
    return df.columns

def guardarDatos(df,ruta,fichero):
    df.to_csv(ruta+fichero)
    return True

def cambiaColumnas(df,columnas):
    df.columns = columnas
    return df

def dameEstadisticos(df,tipo="numerico"):
    """tipo numerico o todos """
    if tipo=='numerico':
        return df.describe()
    else:
        return df.describe(include='all')

def reemplazarNulos(df,columna):
    media = df[columna].mean()
    df[columna].replace(np.nan,media, inplace=True)
    return df

def cambiaTipo(columna,tipo="float64"):
    columna = columna.astype(tipo)
    return columna

def renombrarColumna(df,cambio):
    df.rename(columns = cambio, inplace=True)
    return df

def normalizaColumna(df,columna):
    df[columna] = df[columna]/df[columna].max()
    return df

def obtenerDummies(df,columna):
    df = pd.get_dummies(df[columna])
    return df

""" Datos de prueba para lanzar las pruebas de los metodos"""
if __name__ == '__main__':
    ruta = 'F:\\DAW\\datos\\'
    fichero = 'precios_coches.csv'
    titulos_cabecera = ['indice','nombre','localizacion','año','kilometrosRecorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio']
    df = cargarDatos(ruta,fichero)
    print(df.head(5))
    print(dameColumnas(df))
    guardarDatos(df,ruta,'copia.csv')
    cambiaColumnas(df, titulos_cabecera)
    print(df.columns)
    print(dameEstadisticos(df))
    print(dameEstadisticos(df,'todos'))
    columna = df['indice']
    print(columna.dtype)
    columna = cambiaTipo(columna,'float64')
    print(columna.dtype)
    df = renombrarColumna(df,{'kilometrosRecorridos':'kilometros'})
    print(df.columns)
    print(df['kilometros'])
    df = normalizaColumna(df,'kilometros')
    print(df['kilometros'])
