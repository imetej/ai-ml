import numpy as np
from matplotlib import pyplot as plt

def plot_vector2D(label, vector, color='r', origin=(0,0)):
    origin=np.array(origin)
    vector=np.array(vector)
    plt.quiver(*origin, *vector, color=color, angles='xy', scale_units='xy', scale=1)
    plt.text(*(vector+origin+1), label)

def plot_vector3D(axes, vector, color='r', origin=(0, 0, 0)):
   axes.quiver(*origin, *vector, color=color) 

# vizualize 2d vectors
plt.grid(b=True, which='major')
plt.xlim([-10, 10])
plt.ylim([-10, 10])

v1=[5, 7.5]
v2=[-7.5, 5]
v3=[0, -8]

plot_vector2D("Vector-1", v1, color='r')
plot_vector2D("Vector-2", v2, color='g')
plot_vector2D("Vector-3", v3, color='b')

# vizualize 3d vectors
ax=plt.axes(projection='3d')
plt.xlim([-10, 10])
plt.ylim([-10, 10])
ax.set_zlim(-10, 10)

v1=[1, 2, 3]
v2=[-7, -4, 2]
v3=[3, 4, -2]

plot_vector3D(ax, v1, color='r')
plot_vector3D(ax, v2, color='g')
plot_vector3D(ax, v3, color='b')

# vector addition
plt.grid(b=True, which='major')
plt.xlim([-10, 10])
plt.ylim([-10, 10])

v1=np.array([-2, -5])
v2=np.array([-2, 7])

plot_vector2D("Vector-1", v1, color='r')
plot_vector2D("Vector-2", v2, color='g', origin=v1)
plot_vector2D("Vector-1+ Vector-2", v1+v2, color='b')