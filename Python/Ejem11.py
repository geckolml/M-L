# Ejemplo donde definimos una funcion f()
# en todos los posibles lugares

class g1():
        @staticmethod
        def h1():
                print ("h1() es un metodo")

def h1():
        print ("h1() es una funcion")

def k1():
        def h1():
                print ("h1() es una funcion interna")
        h1()

g1.h1()
h1()
k1()
