# Ejemplo acerca de la probabilidad condicional en Python

import  random

def random_kid():
    return random.choice(["chico", "chica"])

if __name__ == "__main__":

    ambos_chicas = 0
    mayor_chica = 0
    si_es_chica = 0

    random.seed(0)
    for _ in range(10000):
        menor = random_kid()
        mayor = random_kid()
        if mayor == "chica":
            mayor_chica += 1
        if mayor == "chica" and menor == "chica":
            ambos_chicas += 1
        if mayor == "chica" or menor == "chica":
            si_es_chica += 1

    print("P(ambos | mayor):", ambos_chicas / mayor_chica)      
    print("P(ambos | si es chica): ", ambos_chicas / si_es_chica) 