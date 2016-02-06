# Creacion de la secuencia de Fibonacci usando generadores
from itertools import islice 

def fib():
    prev, actual = 0, 1
    while True:
        yield actual
        prev, actual = actual, prev + actual
        
f = fib()
list(islice(f, 0,9))
