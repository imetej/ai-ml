import numpy as np
from matplotlib import pyplot as plt

def plot_vector2D(label, vector, color='r', origin=(0, 0)):
    vector=np.array(vector)
    origin=np.array(origin)
    plt.quiver(*origin, *vector, angles='xy', scale_units='xy', scale=1, color=color)
    plt.text(*(vector+origin+1), label)

v=np.array([8, 6])
w=np.array([-3, 4])

vec_sum = v + w
vec_dot = np.dot(v, w)

vmag=np.linalg.norm(v)
wmag=np.linalg.norm(w)

vec_sum_mag = np.linalg.norm(vec_sum)

vec_dot_mag = np.abs(vec_dot)

print(f'|v| = {vmag:.4f}')
print(f'|W| = {wmag:.4f}')
print()

print(f'|v + w| = {vec_sum_mag:.4f}')
print(f'|v| + |w| = {vmag + wmag:.4f}')

if vec_sum_mag <= vmag+wmag:
    print('|v + w| <= |v| + |W|')
    print(f'{vec_sum_mag:.4f} <= {vmag + wmag:.4f}')
    print('Triangle Inequality is satisfied')
else:
    print('|v + w| > |v| + |W|')
    print(f'{vec_sum_mag:.4f} > {vmag + wmag:.4f}')
    print('Triangle Inequality is not satisfied')
print()

print(f'|v . w| = {vec_dot_mag:.4f}')
print(f'|v| . |w| = {vmag * wmag:.4f}')

if vec_dot_mag <= vmag*wmag:
    print('|v . w| <= |v| . |W|')
    print(f'{vec_dot_mag:.4f} <= {vmag * wmag:.4f}')
    print('Schwarz Inequality is satisfied')
else:
    print('|v . w| > |v| . |W|')
    print(f'{vec_dot_mag:.4f} > {vmag * wmag:.4f}')
    print('Schwarz Inequality is not satisfied')
print()

plt.grid()
plt.xlim([-2, 12])
plt.ylim([-2, 12])

plot_vector2D(f"|v| = {vmag:.4f}", v, color='r')
plot_vector2D(f"|w| = {wmag:.4f}", w, color='g', origin=v)
plot_vector2D(f"|v + w| = {vec_sum_mag:.4f}", vec_sum, color='b')