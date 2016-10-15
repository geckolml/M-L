##  Ejercicios de Python 

1 .  El siguiente programa de Python no es identado correctamente. Reescribe el programa de tal manera que esté indentado correctamente

```python
def dia_1(dia):
if dia == "lunes":
return ":("
if dia != "lunes":
return ":D"

print(dia_1("domingo"))
print(dia_1("lunes"))
```

2 . ¿ Cuál de los siguientes números son enteros válidos en Python? `110, 1.0, 17.5, -39, -2.3`

3 . ¿ Cuáles son los resultados de las siguientes operaciones y explica el por qué de los resultados?

```python
15 +20 *3
```

```python
13 // 2 + 3
```

```python
20% 7 // 3
```

```python
2 ** 3 ** 2
```
4 . ¿ Qué ocurre cuando evaluamos `1 // 0` en la consola de Python?. ¿ Por qué esto ocurre?.

5 . ¿ Cuál de los siguientes son números punto flotante en Python? `1, 1.0, 1.13e4, -3.141759, 735, 0.57721566, 7.5e-3`.

6 .  ¿ Cuál es la diferencia entre división entera y punto flotante?. ¿ Cuál es el operador usado para la división entera? ¿ Cuál es el operador usado para la división punto flotante?.

7 . ¿ Cuáles son los resultados de las siguientes operaciones y explica el por qué de los resultados?

```python
15 // 20 *3
```

```python
13 / 2 * 3
```

```python
20% 7 // 3.2
```

```python
- 3 // 2
```

8  . ¿ Qué ocurre cuando evaluamos `1 / 0` en la consola de Python?. ¿ Por qué esto ocurre?.

9 .  ¿ Qué ocurre cuando evaluamos `1e1000`? ¿Qué hay de `-1e1000` y de `type(1e1000)`?


10 . ¿ Qué produce la siguiente secuencia de código?

```python
nombre = "Cesar Lara-Avila"
print(nombre.lower())
print(nombre)
```
11 . Describe el ámbito (*scope*) de las variables `a, b, c` y `d` en este ejemplo:

```python
def f1(a):
    b = a - 2
    return b

c = 3

if c > 2:
    d = f1(5)
    print(d)
```
12 . Explica lo que hace el siguiente código, línea a línea (Escribe comentarios)

```python
# Definimos algunas opciones

LOWER, UPPER, CAPITAL = 1, 2, 3

nombre  = "milagritos"
estilos = UPPER

if estilos == LOWER:
    print(nombre.lower())
elif estilos == UPPER:
    print(nombre.upper())
elif estilos == CAPITAL:
    print(nombre.capitalize())
else:
    
    print("estilo desconocido!")

```

13 . Detalla las declaraciones del siguiente código

```python
import math
i = math.ceil(5.834)
j = math.floor(5.834)
k = math. round(5.384)
```
14 . Explica el siguiente código y corrige alguna declaración si es que hubiese alguna escrita de forma incorrecta

```python
print(5)
print(6.7)
print("3" + 4)
print("3%d" % 4)
print(int("3") + 4) 
print("3%d" % 4)
print("3" + str(4))
int("3")
int("3.7") 
int(float("3.7"))
```
15 . Las lista y diccionarios son mutable, además de muchos de los objetos que podamos escribir. Explica el código siguiente

```python
lista1 = [1, 2, 3]
lista1[0] = 5
print(lista1)

class Ejemplo(object):
    pass
    
nuevo_objeto = Ejemplo()

nuevo_objeto.propiedad = 42
```

16 . Explica el siguiente código línea por línea

```python
PRECIO_PETROLEO_POR_LITRO = 4.50

print("*** Soy un calculador de eficiencia de combutible! ***\n")
nombre = input("Ingresa tu nombre : ")

distancia_viajada = float(input("Ingresa la distancia que viajastes en km: "))
cantidad_pagada = float(input("Ingresa cuanto pagastes por el combustible en tu viaje : R"))

combustible_consumido = cantidad_pagada / PRECIO_PETROLEO_POR_LITRO

eficiencia_l_por_100_km = combustible_consumido / distancia_viajada * 100
eficiencia_km_por_l = distancia_viajada / combustible_consumido

print("Hi, %s!" % nombre)
print("La eficiencia de tu coche es  %.2f litros por 100 km." % eficiencia_l_por_100_km)
print("Esto siginifica que tu coche puede viajar %.2f km por litro de combustible." % eficiencia_km_por_l)

# Usamos la secuencia de escape \n para dejar un mensaje
print("\nGracias por usar el programa.")

```

17 . Escribe una función que convierte una temperatura dada en grados Fahrenheit a su equivalente en grados Celsius. Tu programa debe pedirle al usuario por un valor de entrada (grado Fahrenheit) y devuelva una salida (grado Celsius).

18 . ¿ Cuál es la salida del siguiente fragmento de código?. Explica

```python
x = 2

if x > 3:
    print("Este numero ")
print("es mayor")
print("que 3.")
```

19 . ¿Cómo podemos simplificar estos fragmentos de código?

```python
if bool(a) == True:
    print("a es verdadero")
```

```python
if x > 50:
    b += 1
    a = 5
else:
    b -= 1
    a = 5
```

20 . ¿Para qué valores  de `x` se imprime el valor de `True`?

```python
if x > 1 or x <= 8:
    print("True")
```

21 . Reescribe el siguiente fragemento de código, usando declaraciones `elif`

```python
if temperatura < 0:
    print("Super helado")
else:
    if temperatura < 10:
        print("Muy frio")
    else:
        if temperatura < 20:
            print("frio")
        else:
            if temperatura < 30:
                print("caliente")
            else:
                if temperatura < 40:
                    print("Caluroso")
                else:
                    print("Super caluroso")

```

22 .Escribe un programa que utiliza un bucle `while` para sumar los cuadrados (a partir de 1) de números  hasta que el total sea mayor  a 200. Imprime el resultado final y el último número al cuadrado agregado.

23 . Explica que hace el siguiente código

```python
numeros = [1, 5, 2, 12, 14, 7, 18]

doble = []
for numero in numeros:
    doble.append(2 * numero)

numeros_pares = []
for numero in numeros:
    if numero % 2 == 0:
        numero_pares.append(numero)

animalitos = ['aardvark', 'cat', 'dog', 'opossum']

animalitos_a = []
for animalito in animalitos:
    if animalito[0] in 'aeiou':
        animalitos_a.append(animalito.title())
```
24 . Encuentra las fuentes potenciales de **errores de ejecución** en este fragmento de código:

```python
for x in range(a, b):
    print("(%f, %f, %f)" % my_list[x])
```

25 . Encuentra las fuentes potenciales de **errores lógicos** en este fragmento de código:

 ```python
 producto = 0
for i in range(10):
    producto *= i

sum_cuadrados = 0
for i in range(10):
    i_sq = i**2
sum_cuadrados += i_sq

nums = 0
for num in range(10):
    num += num
 ```
