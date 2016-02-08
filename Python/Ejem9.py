# Ejemplo del uso de una funcion en Python

"""
Este script muestra como trabajar con 
funciones en Python
"""

def muestra_nombre_modulo():
        print (__doc__)

def archivo_modulo():
        return __file__

x = muestra_nombre_modulo()
y = archivo_modulo()

print(x ,y)
