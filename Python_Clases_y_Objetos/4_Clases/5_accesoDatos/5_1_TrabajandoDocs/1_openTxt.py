# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 08:45:17 2023

@author: pedro
"""

doc = open (r'C:\Users\pedro\OneDrive\Documents\GitHub\CursoObjetos\Python_Clases_y_Objetos\4_Clases\5_accesoDatos\5_1_TrabajandoDocs\datos\holaMundo.txt')
docText = doc.read()
print(docText)
doc.close()