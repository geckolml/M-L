# Ejemplo sobre el uso de la palabra reserva yield y
# el metodo next en los generadores

def fg():
    print ("inicio")
    for i in range(3):
        print ("antes de yield", i)
        yield i
        print ("despues de yield", i)
    print (" fin")
    
