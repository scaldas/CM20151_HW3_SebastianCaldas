import os
os.system('sed "s/,/+/g" Notas.csv > Notas.dat')
os.system('echo "Se ha impreso Notas.dat usando comandos de la terminal"')

