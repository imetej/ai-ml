import numpy as np
from matplotlib import pyplot as plt
A = np.array([[2,5],[3,6]])
y = np.array([20,12])
x = np.linalg.solve(A,y)
print(f'A = \n{A}')
print(f'y = \n{y}')
print(f'x = \n{x}')
print(f'Is Ax = y : {np.allclose(np.dot(A,x),y)}')

A = np.array([[2,5],[3,6]])
y = np.array([20,12])
x = np.matmul(np.linalg.inv(A),y)
xplot = np.linspace(-30,30,3)
yplot1 = (20-2 * xplot) / 5
yplot2 = (12-3 * xplot) / 6
plt.plot(xplot,yplot1)
plt.plot(xplot,yplot2)
plt.legend(['2x+5y=20','3x+6y=12'])