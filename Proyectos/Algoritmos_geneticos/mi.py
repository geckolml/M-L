# -*- coding: utf-8 -*-
import random as r
#indice en la tupla
#tu : Lista de tuplas a buscar
#va : valo que se quiere buscar
def indice(tu,va):
	n = len(tu)
	#print "indice:",tu,va
	i=0
	while i < n:
		if tu[i][0] >= va:
			return i
		i += 1
	return -1
# lt :lista de tuplas
# x  : cantidad a marcar
def marcar(lt,x):
	#lt esta ordenado
	n = len(lt)
	if x > n:
		print "Cantidad excedido"
		return -1
	#quitar 5
	s = 0
	b = []
	for i in range(n):
		b.append(0)
		s+=lt[i][0]
	j=0
	#print 'while'
	while j<x:
		ra = int(r.random()*s)
		k = indice(lt,ra)
		#print '>>',k,ra,n,x
		#print lt
		#print b
		#print s,ra
		if (k > -1)&( b[k]==0):
			b[k]=1
			j += 1
	return b

def inicio():
	#a=[(3,2),(35,2),(45,2)]
	a =[(3,0),(35,0),(45,0)]
	b=marcar(a,2)
	print ">>"
	print a,b
	print "<<"
#inicio()
