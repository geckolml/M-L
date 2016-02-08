# Uso de la funcion dir() en el espacio de nombres
# del modulo

"""
Este es un modulo de ejemplo para el
uso de la funcion dir()
"""

import math, sys

x = math.sin(20)

lenguajes = ["Python", "R","Java", "C", "Make"]

def mostrar_lenguajes():
    for i in lenguajes:
        print (i)

print (dir(sys.modules['__main__']))

