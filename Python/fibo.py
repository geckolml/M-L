# Modulo conteniendo la funcion de fibonacci

"""
Modulo que contiene una funcion que genera
la secuencia de Fibonacci
"""

def fib(n):
    x ,y =0, 1
    while y < n:
        print (y)
        (x , y) = (y, x +y)
        
# Prueba
        
if __name__ == '__main__':
    fib(500)