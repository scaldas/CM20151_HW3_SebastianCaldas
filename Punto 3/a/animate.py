import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

filenames = []
num = 0

x = []
y = []

for filename in os.listdir('Test'):
    filenames.append(filename)

dat = np.loadtxt('Test/test05800.txt')
for registro in dat:
	x.append(registro[0])
	y.append(registro[1])

fig = plt.figure()
line, = plt.plot(x, y, ".")

def init():
    line.set_data([], [])
    return line,

def animate(i):
	global num 
	if num >= len(filenames):
		num = 0
	dat = np.loadtxt('Test/' + filenames[num])
	x = []
	y = []
	for registro in dat:
		x.append(registro[0])
		y.append(registro[1])
	line.set_data(x, y)
	num = num + 1
	return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=20, blit=False)
plt.show()