import numpy as np
import matplotlib.pyplot as plt

Datos = np.genfromtxt('d.txt')

x = Datos[:,0]
y = Datos[:,1]

plt.plot(x, y)
plt.savefig('grafica.pdf')
plt.show()

