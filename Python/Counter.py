import collections
from collections import defaultdict

lenguaje_lista = 'R Python Haskell C Latex'.split()
lenguaje_contador = defaultdict(int)  # El valor por defecto de int es 0

for lenguaje in lenguaje_lista :
    lenguaje_contador[lenguaje] += 1
    
lenguaje_contador

lista1_ = defaultdict(list)  # Lista vacia
lista1_["Java"].append(1)
lista1_

# Otro ejemplo

dict1_ = defaultdict(dict)   #diccionario vacio
dict1_["Cesar"]["Ciudad"] = "Lima"

dict1_


# Para el caso de funciones

fun1_ = defaultdict(lambda: [0, 0])
fun1_[2][1] = 1
fun1_


print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print (collections.Counter({'a':2, 'b':3, 'c':1}))
print (collections.Counter(a=2, b=3, c=1))



d = collections.Counter('abbeeddaabbbccc')
for letra in 'abcdef':
    print ('%s: %d' %(letra, d[letra]))
    
    

c = collections.Counter()
with open('Svm.txt', 'rt') as f:
    for linea in f:
        c.update(linea.rstrip().lower())
        
print("Mas comunes")
for letra, contador in  c.most_common(5):
    print('%s: %7d' % (letra, contador))
    
    
    
    
    
mis_lenguajes= ['R', 'Python', "C++", "JavaScript"]
for i, lenguajes in enumerate(mis_lenguajes, 1):
    print(i, lenguajes)
    
    
    
lista1= ['Erika', 'Delia', 'Milagros']
lista2 = [1, 2, 3]
lista = zip(lista1, lista2)
list(lista)


chicas = [('Erika', 1), ('Delia', 2), ('Milagros', 3)]
lista1, lista2 = zip(*chicas)
lista1


s = set()
s.add(1)  # s es ahora { 1 }   
s.add(2)  # s es ahora { 1, 2 }
s.add(2)  # s es aun  { 1, 2 }
x = len(s) # igual a 2
y = 2 in s # igual a  True
z = 3 in s # igual a  False
x, y, z


alguna_lista = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicados = set([x for x in alguna_lista if alguna_lista.count(x) > 1])
print(duplicados)

item_lista = [1, 2, 3, 1, 2, 3, 4, 5, 5,]
num_items = len(item_lista)
item_set = set(item_lista)
num_distintos_items = len(item_set)
distintos_item_lista = list(item_set)

num_items, item_set, num_distintos_items, distintos_item_lista

