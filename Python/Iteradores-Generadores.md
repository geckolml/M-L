# Iterables, Iteradores  y Generadores

*Notas basadas en el artículo de Vincent Driessen: Iterables vs iterators vs Generators*

## Contenedores 

Los contenedores son  estructuras de datos, que contienen elementos y suporta pruebas de permanencia de sus elementos. Son estructuras de datos que viven en la memoria y almacenan sus valores en memoria también. En Python algunos ejemplo son:

1 . **list**, `deque , ...`

2 . **set**, `frozensets, ...`

3 . **dict**, `default, OrderedDict, Counter, ...`

4 . **tuple**, `namedtuple, ...`

5 . **str**

Un objecto es un `contenedor`, cuando podemos preguntar si contiene un cierto elemento. Podemos llevar esas pruebas de pertenencia sobre listas, conjuntos (sets) o tuplas, de la siguiente manera:

```python
assert 1 in [1, "R", 2, "JS"]      # listas
assert 4 not in [1, 2, 3, 7]
assert 1 in {1, 2, 3}      # sets
assert 4 not in {1, 2, 3}
assert 6 in (2, 4, 6, 8)      # tuplas
assert 4 not in (1, 2, 3)
```

En el caso de los diccionarios

```python
d = {1: 'python', 2: 'R', 3: 'C++'}
assert 1 in  d
assert 5 in d
assert 'C++' not in d
```


Podemos preguntas si una cadena, contiene una subcadena

```python
s = 'spandueballett'
assert 'a' in s
assert 'b' not in s
assert 'ball' in s
```


Las cadenas literalmente no almacenan copias de todas sus subcadenas de memoria, pero se pueden usar de esta manera.


Aunque la mayoria de los contenedores proporcionan una manera de producir, todos los elementos  que contiene, esta capacidad, no le hace a ellos un contenedor sino un iterable.

**No todos los contenedores son iterables**. Un ejemplo de esto es  un  [Bloom Filters](http://billmill.org/bloomfilter-tutorial/), una estructura de datos probabilistica, que permite que se le pregunte si contiene un determinado elemento, pero no es capáz de retornas sus elementos individuales.

## Iterables 

La mayoría de los contenedores también son iterables. Pero muchas cosas más son también iterables . Ejemplos de ello son los archivos abiertos, sockets  abiertos, etc. Donde  los  contenedores  son típicamente finitos, un iterable puede  también  representar  una fuente infinita de datos.

Un iterable es cualquier objeto, no necesariamente una estructura de datos, que puede devolver un ** iterador** (con el fin de devolver todos los elementos). Eso suena un poco incómodo, pero hay una diferencia importante entre un iterable y un iterador.  Vemos este ejemplo:

```python
x = [1, 2, 3]
y = iter(x)
z = iter(x)
next(y)
1
next(y)
2
next(z)
1
type(x)
<class 'list'>
type(y)
<class 'list_iterator'>
```

Aquí, `x` es el iterable, mientras que `y` y `z` son instancias individuales de un iterador, produciendo valores desde el iterable `x`. Ambos `y` y `z` mantienen un estado como se muestra en el ejemplo.

A menudo, las clases iterables implementarán tanto `_iter__()` y `__next__` en la misma clase y tener `__iter__()` devolviendo `self`, lo que hace de la clase un iterable y su propio iterador. Es correcto retornar diferentes objetos como iteradores sin embargo.

Cuando se escribe :

```python
x = [1, 2, 3]
for elem in x:
...
```

lo que ocurre es lo que se muestra en el siguiente gráfico:

![](iterable-vs-iterator.png)


Cuando desensamblamos este código en Python, se puede ver la llamada explícita a `GET_ITER`, que es esencialmente igual a la invocación `iter(x)`. `FOR_ITER` es una instrucción que va a hacer el equivalente a llamar  `next()` repetidamente para obtener todos los elementos, pero esto no se demuestra en  las instrucciones de código de bytes porque está optimizada para la velocidad en el intérprete.
```python
import dis
x = [1,2,3]
dis.dis('for _ in x: pass')

1           0 SETUP_LOOP			14( to 17)
			3 LOAD_NAME				0(x)
            6 GET_ITER
		>>  7 FOR_ITER				 6(to 16)
			10 STORE_NAME 			 1 (_)
            13 JUMP_ABSOLUTE		 7
        >>  16 POP_BLOCK
        >>  17 LOAD_CONST
            20 RETURN VALUE
```

## Iteradores 

Un iterador es un objeto auxiliar de 'estado' que producirá el siguiente valor cuando se llama a `next()` en el. Un objecto que tiene un método `__next__` es por tanto un iterador.

Cada vez que se pide por el próximo valor (next), este sabe como calcularlo ya que esta sujeto a estados internos.

Todas  las funciones de [itertools](https://docs.python.org/3/library/itertools.html) retornan iteradores. Algunas producen secuencias infinitas:

```python
from itertools import count
contador = count(start =3)
next(contador)
3
next(contador)
4
next(contador)
5
```

Algunas producen infinitas secuencias, desde finitas secuencias

```python
from itertools import cycle
lenguajes = cycle(['Python', 'R', 'C++'])
next(lenguajes)
'Python'
next(lenguajes)
'R'
next(lenguajes)
'C++'
next(lenguajes)
'Python'
```

Algunas producen secuencias finitas, desde infinitas secuencias

```python
>>> from itertools import islice
>>> lenguajes = itertools.cycle(['Python', 'R', 'C++'])  # infinito
>>> lim = islice(lenguajes, 0, 4)                          # finito
>>> for x in lim:                         # modo seguro de usar el bucle for
...     print(x)
Python
R
C++
Python
```


Para tener una mejor idea de los detalles internos de un iterador, vamos a construir un iterador que produce los números Fibonnaci.


```python
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
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

```

Tenga en cuenta que esta clase es a la vez un iterable ( tiene el método `__iter __ ()`) y su propio iterador (tiene un método `__next __ ()`).

El estado dentro de este iterador se  mantiene dentro de las variables de instancia  `prev` y `actual` y se utilizan para   subsecuentes llamadas al iterador. Cada llamada a `next()` realiza dos importantes cosas:

1 . Modifica el estado para la siguiente llamada a `next()`.
2 . Presenta el resultado para la actual llamada.


Desde el exterior, el iterador es como una fábrica 'perezosa'  que está inactiva hasta que se le  pide para un valor, que es cuando comienza a funcionar y produce un solo valor, después del cual se vuelve inactiva de nuevo.

En Python, podemos definir un iterador es un objeto que implementa el `protocolo iterador` que consiste de los métodos mencionados `__iter__()` que retorna el objeto iterador y `__next__()` que retorna el elemento siguiente de una secuencia. Python tiene varios objetos, que implementan el `protocolo iterador`, como las listas, tuplas, diccionarios o archivos.

```python
# Ejemplo del uso de iteradores con archivos

#!/usr/bin/python

f = open('python.txt', 'r')

for linea in f:
    print (linea)
    
f.close()
```

## Generadores 

Los generadores son un tipo especial de iterador. Los generadores te permiten escribir iteradores al igual que el ejemplo de secuencia  de los números de Fibonacci, dada anteriormente, pero una sucinta sintaxis, que evita escribir clases con los métodos `__iter__()` y `__next__()`. En general

1 . Un generador es un iterador, pero no se cumple lo contrario.
2 . Un generador, por tanto es como una fábrica ('perezosa') que produce valores, en realidad una secuencia de valores.

Aquí la misma secuencia de números de Fibonacci, usando generadores

```python
# Creacion de la secuencia de Fibonacci usando generadores
from itertools import islice 

def fib():
    prev, actual = 0, 1
    while True:
        yield actual
        prev, actual = actual, prev + actual
        
f = fib()
list(islice(f, 0,9))
[1, 1, 2, 3, 5, 8, 13, 21, 34]
```


Expliquemos paso a paso que sucede en el programa anterior : en primer lugar, debemos darnos cuenta que **fib** se define como una función de Python, nada especial. Nótese, sin embargo, que no hay la  palabra clave `return` dentro del cuerpo de la función. El valor de retorno de la función será un generador (es decir: un iterador, una fábrica, un objeto auxiliar de estado).

Ahora, cuando `f = fib()` se llama, el generador (la fábrica) es instanciado y retornado . Ningún código se ejecutará en este punto: el generador comienza en un estado inactivo inicialmente. Para ser explícitos: la línea 

`prev, actual = 0, 1`

no se ejecuta todavía.

Entonces, esta instancia del generador es envuelto en  `islice()`. Este es en sí también un iterador. No pasa nada, todavía.

Entonces, este iterador es envuelto en  `list()`, que usará todos sus argumentos y crea una lista  de estos. Para ello, se empieza a llamar a `next()` en la instancia `islice()`, que a su vez empieza a llamar a `next()` en nuestro instancia `f`.

Sin embargo, un paso a la vez. En la primera invocación, el código  finalmente correrá un poco: `prev, curr = 0, 1` es ejecutado, ingresamos entonces  en el bucle `while True`, y luego nos encontramos la declaración `yield actual`.

Esta producirá el valor que está actualmente en la variable `actual` y se volverá inactiva  otra vez. Este valor se pasa a `islice()`, que producirá este valor (porque no se a ido más allá del 9 todavia) y la lista puede agregar el valor 1 a la lista ahora.

A continuación, se pide a `ìslice` por el valor siguiente, el cual le pedirá a `f` por el valor siguiente, esto deberá "quitar la pausa" de f desde su estado anterior, reanudando con la declaración ` prev, actual  = actual, prev + actual`. Luego se vuelve a entrar en la siguiente iteración del bucle `while`, y alcanzamos la declaración `yield actual`, devolviendo el siguiente valor de `actual`.

Esto ocurre hasta que la lista tenga 9 elementos y cuando `list()` pide a `islice()` por el valor 10, `islice()` provocará una excepción `StopIteration`, lo que indica que el final se ha alcanzado, y la lista devolverá el resultado: una lista  que contienen los 9 primeros números de Fibonacci.

Se debe notar que el generador no recibe la llamada 10 de `next()`. De hecho, no se volverá a utilizar, y será basura recogida más tarde.



Mostremos otro ejemplo, para clarificar mejor la relación entre `yield` y la llamada al método `next` sobre el generador

```python
def fg():
    print ("inicio")
    for i in range(3):
        print ("antes de yield", i)
        yield i
        print ("despues de yield", i)
    print (" fin")

f = fg()
next(f)
inicio
antes de yield 0
0

next(f)
despues de yield  0
antes de yield 1
1

next(f)
despues de yield 1
antes de yield 2
2

next(f)
despues de yield 2
 fin
Traceback (most recent call last):

  File "<ipython-input-43-468f0afdf1b9>", line 1, in <module>
    next(f)

StopIteration
```



### Tipos de Generadores

Hay dos tipos de generadores en Python: las funciones generadoras y los generadores  de expresiones. Una función generadoras  es cualquier función en la que  rendimiento de palabra clave `yield` aparece en su cuerpo. Acabamos de ver un ejemplo de ello. El aspecto de la  palabra clave `yield` es suficiente para hacer de la función  una función generadora.

El otro tipo de generador es el generador equivalente de una lista por comprensión. Su sintaxis es muy elegante para de uso limitado

Supongamos que se utiliza esta sintaxis para crear una lista de números:

```python
numeros = [1 ,2 ,3 ,4 ,5]
[x * x for x in numeros]
[1, 4, 9, 16, 25]
```

Se puede hacer lo mismo haciendo  usando un  conjunto por comprensión:

```python
{x*x for x in numeros}
{1, 4, 9, 16, 25}
```
 o usando diccionarios
 
 ```python
{x: x *x for x in numeros}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
 ```

Pero también se puede usar una expresión generadora:

```python
>>> cuadrados= (x * x for x in numeros)
>>> cuadrados
<generator object <genexpr> at 0x10d1f5510>
>>> next(cuadrados)
1
>>> list(cuadrados)
[4, 9, 16, 25]
```

Tenga en cuenta que, debido a que hemos leido el primer valor de `cuadrado` con `next ()`, su estado se encuentra ahora en el "segundo" item, por lo que cuando recorramos la totalidad de las llamadas a `list()`, sólo se devolverá una lista de `cuadrados` parcial, empezando por el segundo valor.