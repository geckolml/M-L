# Ejemplo acerca del manejo de excepciones en Python 

def numero_flotante():
    "Devuelve un numero flotante"
    numero = float(input("Ingresa un numero flotante: "))
    return numero

while True:
    try:
        print(numero_flotante())
    except ValueError:
        print("Has ingresado un valor incorrecto")