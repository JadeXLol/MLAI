import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = [1, 2, 3, 1]
y = [1, 3, 1, 1]

#x = []
#y = []
#for i in range(3):
#    x.append(i)
#    y.append(i)


plt.plot(x,y)


for xy in zip(x,y):
    ax.annotate(text=f'{xy}', xy = xy, textcoords='offset points', xytext=(5,5))

plt.xlabel('x')
plt.ylabel('y')

min_x = 0
max_x = 10
min_y = 0
max_y = 10
step = 1
ax.set_xticks(np.arange(min_x, max_x, step=step))
ax.set_yticks(np.arange(min_y, max_y, step=step))

plt.grid(linestyle='--')

plt.gca().set_aspect('equal')

plt.show()