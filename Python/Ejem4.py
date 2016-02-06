# Iterador que produce los numeros de Fibonacci
from itertools import islice

class fib:
    def __init__(self):
        self.prev = 0
        self.actual = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        valor = self.actual
        self.actual += self.prev
        self.prev = valor
        return valor
        
f = fib()
list(islice(f, 0,12))
        