import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns

#Scatter Plots
tips = sns.load_dataset("tips")
plt.scatter(tips["total_bill"],tips["tip"])
plt.show()

#box plot
sns.set_theme(style="whitegrid")
fig = sns.boxplot(x=tips['total_bill'])
plt.show()

#heat map
my_map = np.random.randn(10,10)
plt.imshow(my_map)
plt.colorbar()
plt.show()

#Contour Plot
x = np.linspace(-3.0,3.0,100)
y = np.linspace(-3.0,3.0,100)
X,Y = np.meshgrid(x,y)
Z = np.sqrt(X**2+Y**2)
fig, ax = plt.subplots(1,1)
p = ax.contour(X,Y,Z)
fig.colorbar(p)
ax.set_title("Contour Plot")
ax.set_xlabel("x(cm)")
ax.set_ylabel("y(cm)")
plt.show()

#3D surface plot
x = np.outer(np.linspace(-3,3,32), np.ones(32))
y = x.copy().T
z = (np.sin(x**2) + np.cos(y**2))
fig = plt.figure(figsize = (14,9))
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z)
plt.show()

import numpy as np

heights = np.random.normal(1.75,0.1,25)
heights = np.round(heights,2)
print('Mean = ', heights.mean())
print('Standard Deviation = ', heights.std())
print('Variance = ', heights.var())