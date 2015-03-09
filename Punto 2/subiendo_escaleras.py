import sys
import numpy as np

mapa = {1:1, 2:2}

def posibilidades(n):
	#Subir una escalera de 0 escalones es trivial.
	if n == 0:
		return 1
	if(n in mapa):
		return mapa[n]
	pos_uno_menos = 0
	pos_dos_menos = 0
	if(n-1 in mapa):
		pos_uno_menos = mapa[n-1]
	else:
		pos_uno_menos = posibilidades(n-1)
		mapa[n-1] = pos_uno_menos
	if(n-2 in mapa):
		pos_dos_menos = mapa[n-2]
	else:
		pos_dos_menos = posibilidades(n-2)
		mapa[n-2] = pos_dos_menos
	return pos_uno_menos + pos_dos_menos

def escaleras(A, B):
	C = np.zeros(len(A))
	rta = []
	for i in range(0, len(A)):
		C[i] = A[i]%(2*B[i])
	for i in range(0,len(C)):
		num = C[i]
		if num > 1000:
			j = 0
			while j < num:
				posibilidades(j)
				j = j + 500
		rta.append(posibilidades(num))
	return rta

print('Hay ' + str(posibilidades(13)) + ' maneras diferentes de subir una escalera de ' + str(13) + ' escalones.')
print('Hay ' + str(posibilidades(15)) + ' maneras diferentes de subir una escalera de ' + str(15) + ' escalones.')
user_input = input("Que otro numero quieres averiguar? (Escribe -1 para continuar al siguiente literal) ")

while int(user_input) != -1:
	if user_input > 1000:
		i = 0
		while i < user_input:
			posibilidades(i)
			i = i + 500
	print('Hay ' + str(posibilidades(int(user_input))) + ' maneras diferentes de subir una escalera de ' + str(user_input) + ' escalones.')
	user_input = input("Que otro numero quieres averiguar? (Escribe -1 para continuar al siguiente literal) ")

print('Fin del literal a')
print('Inicio del literal b')

A = input("Escribe el arreglo A (Escribelo como '[1,2,3]', con los corchetes) ")
B = input("Ahora escribe el arreglo B (de nuevo como '[1,2,3]', con los corchetes) ")

if len(A) != len(B):
	sys.exit("ERROR: Los arreglos deben tener el mismo numero de elementos.")

rta = escaleras(A,B)
print('El arreglo resultante de la funcion escalera es:')
print(rta)
print('Fin del literal b')
