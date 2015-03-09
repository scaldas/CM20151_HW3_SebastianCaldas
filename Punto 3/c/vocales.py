# coding=UTF-8
import sys

if(len(sys.argv) != 2):
	print("Usage: python vocales.py numlineas")
	exit(1)

baud = open('Sainte-Beuve.txt', 'r')
head = [next(baud) for i in range(0,int(sys.argv[1]))]

#	Para este ejercicio no se considero la y como vocal, asi lo pueda ser foneticamente.
#	Si se toman como vocales: æ y œ
for line in head:
	count = 0
	for letter in line.decode('utf-8'):
		if letter in 'aeiouáéíóúàèìòùâêîôûäëïöüAEIOUÁÉÍÓÚÀÈÌÒÙÄËÏÖÜÂÊÎÔÛæœ'.decode('utf-8'):
			count = count + 1
	print(count)

baud.close()