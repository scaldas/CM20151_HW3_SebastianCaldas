old_file = open('Notas.csv', 'r')
new_lines = []
#Es + o es espacio????!!!!!
for line in old_file:
	new_lines.append(line.replace(',','+'))
old_file.close()


new_file = open('Notas.dat', 'w')
for new in new_lines:
	new_file.write(new)
new_file.close()

print("Se ha impreso Notas.dat")