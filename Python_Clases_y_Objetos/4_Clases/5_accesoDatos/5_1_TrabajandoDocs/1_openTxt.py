# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 08:45:17 2023

@author: pedro
"""
import re
doc = open (r'C:\Users\pedro\OneDrive\Documents\GitHub\CursoObjetos\Python_Clases_y_Objetos\4_Clases\5_accesoDatos\5_1_TrabajandoDocs\datos\holaMundo.txt')
docText = doc.read()
print(docText)
doc.close()
print(docText)
doc = open (r'C:\Users\pedro\OneDrive\Documents\GitHub\CursoObjetos\Python_Clases_y_Objetos\4_Clases\5_accesoDatos\5_1_TrabajandoDocs\datos\holaMundo.txt','a')
doc.write("\n" + docText)
patron = r'\s+'
resultado = re.sub(patron, '', docText)
print(resultado)
print(len(resultado))

doc.close()