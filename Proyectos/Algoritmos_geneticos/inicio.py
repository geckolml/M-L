# -*- coding: utf-8 -*-
import math
import random as r
import mi
# _tp : tamaño de la población
_tp = 10
#_pob = [3,4,12,3,1,2,5,2,4,2]
_pob = []
#_pro = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
_pro = []
# seleccion
def fun(x):
	#return 354.0 - (x-1)*(x-1)
	return 354.0 - (x-200)*(x-200)
	#return 100.0 -(x-1)*(x-10)*(x-20)*(x-30) # 25 5
#Valor máximo
def fitness(x):
	return fun(x)
def verPoblacion():
	#for i in _pob:
	#	print bin(i),"\t\t",i,"\t",fitness(i)
	i = 0
	n = len(_pob)
	while i < n:
		print bin(_pob[i]),'\t\t\t',_pob[i],fitness(_pob[i]),'\tprob\t',_pro[i]
		i += 1
def inicializar():
	#print 'Inicializar'
	#rangos
	l = _tp
	for i in range(l):
		rango = 1000
		a = int(r.random()*rango-rango/2)
		#_pob.append(100)
		_pob.append(a)
		_pro.append(1)
def evaluar():
	#print 'Evaluar'
	suma = 0.0
	n = len(_pob)
	#buscar el menor
	cota = _pob[0]
	for i in _pob:
		if i < cota:
			cota = i
	
	for i in _pob:
		suma += (fitness(i)-cota)
		
	#asume suma > 0
	for i in range(n):
		dis = (fitness(i) - cota)
		_pro[i] = 1 + int(10000.0*(dis/suma)) # esto afecta a 'Error no puede ser 0'
		#_pro[i] = 1 + int(100000000.0*(dis/suma)) # esto afecta a 'Error no puede ser 0'

def seleccion(x):
	#print 'Selección'
	n = len(_pob)
	a =[]
	s = 0
	#print 'aa1',len(_pob),len(_pro)
	#print 'sel.for'
	for i in range(n):
		#print 'sel.for.i=',i,' n=',n
		if _pro[i]==0:
			print 'Error no puede ser 0'
			return
		s += _pro[i]
		a.append((s,0))
	#print 'sel.mi.mar'
	b = mi.marcar(a,x)
	return b
def cruce(b):
	#print 'Cruce'
	#print '>>es>>'
	a1 = -1
	a2 = -1
	i = 0
	n = len(_pob)
	while i < n:
		if b[i] == 1:
			a1 = i
			i += 1
			while i < n:
				if b[i] == 1:
					a2 = i
					# mascara mas
					mas = int(r.random()*1000)
					#print bin(mas),'\t',mas
					r1 = a1 & mas
					r2 = a2 & ( mas ^ ( ( 1 << 10) - 1 ) )
					res = r1 | r2
					_pob.append(res)
					_pro.append(1)
					
					r1 = a2 & mas
					r2 = a1 & ( mas ^ ( ( 1 << 10) - 1 ) )
					res = r1 | r2
					_pob.append(res)
					_pro.append(1)
				i += 1
		i  += 1
def mutacion(b):
	a1 = -1
	a2 = -1
	i = 0
	n = len(_pob)
	while i < n:
		if b[i] == 1:
			# mascara mas
			mas = int(r.random()*1000)
			a = _pob[i]
			
			#r1 parte a cambiar
			r1 = a & mas
			a1 = ( r1 ^ ( ( 1 << 10) - 1 ) )
			#r2 parte constante
			r2 = a & ( mas ^ ( ( 1 << 10) - 1 ) )
			# a1 | r1
			res = a1 | r2
			_pob.append(res)
			_pro.append(1)
		i  += 1
def reducir():
	b=seleccion(_tp)
	n = len(_pob)
	i = n-1
	while i >=0:
		if b[i]==0:
			_pob.pop(i)
			_pro.pop(i)
		i -= 1
def  algoritmo(lim):
	print "Algoritmo Genetico"
	inicializar()
	evaluar()
	print 'Poblacion inicial'
	verPoblacion()
	i = 0
	while i < lim :
		a=int(_tp*0.8)
		b=seleccion(a)
		cruce(b)
		a=int(_tp*0.2)
		b=seleccion(a)
		mutacion(b)
		reducir()
		evaluar()
		#print "Generación ",i
		#verPoblacion()
		i += 1
	print '\nPoblación final : ',lim
	verPoblacion()

def inicio():
	print 'Problación inicial'
	#verPoblacion()
	#print bin(7)
	gener = 20
	algoritmo(gener)
	#print 'Problación Generacion ',gener
	#verPoblacion()
	#verPoblacion()
inicio()
