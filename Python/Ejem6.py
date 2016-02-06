# Los iteradores son implementados como clases. Aqui un iterador
# que trabaja como la funcion x-range

class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
        
    def __iter__(self):
        return self
        
    def next(self):
        if self.i < self.n:
            i = self.i
            self.i +=1
            return i
        else:
            raise StopIteration()
            
# Ejecutemos el programa
#y = yrange(3)
#y.next()    # 0
#y.next()    # 1
#y.next()    # 2
#y.next()    # Aparece la excepcion StopIteration
            