# Ejemplo del uso de iteradores con archivos

#!/usr/bin/python

f = open('python.txt', 'r')

for linea in f:
    print (linea)
    
f.close()