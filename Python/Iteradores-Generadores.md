# Iterables, Iteradores  y generadores 


## Contenedores 

Los contenedores son  estructuras de datos, que contienen elementos y suporta pruebas de permanencia de sus elementos. Son esstructuras de datos que viven en la memoria y almacenan sus valores en memoria también. En Python algunos ejemplo son:

1 . **list**, `deque , ...`
2 . **set**, `frozensets, ...`
3 . **dict**, `default, OrderedDict, Counter, ...`
4 . **tuple**, `namedtuple, ...`
5. **str**

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














