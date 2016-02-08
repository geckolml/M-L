# Las funciones en Python son objetos.

def f():
        """ Esta funcion imprime un mensaje"""
        print ("Python es un lenguaje tan importante como R")

print (isinstance(f, object)) # Se verifica si f() es una instancia de object.
print (id(f))

print (f.__doc__)
print (f.__name__)
