class Animalito():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def decir_algo(self):
        print ("Yo soy" + self.nombre)

class Perrito(Animalito):
    def decir_algo(self):
        print ("Yo soy  "  + self.nombre \
               + ", y puedo ser tu amigo")

perrito = Perrito("kapu")
perrito.decir_algo()
