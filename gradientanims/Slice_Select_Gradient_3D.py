import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


x, y, z = np.meshgrid(np.linspace(-3, 3, 10), np.linspace(-3, 3, 10), np.linspace(-3, 3, 10))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


u = np.ones_like(x)
v = np.zeros_like(y)
w = np.zeros_like(z)


theta = 0


def update(frame):
    global theta
    theta += np.pi / 30  
    

    mask = np.logical_and(x >= -1, x <= 1)
    u[mask] = 0
    v[mask] = np.cos(theta)
    w[mask] = np.sin(theta)
    
    ax.clear()
    ax.quiver(x[mask], y[mask], z[mask], u[mask], v[mask], w[mask], color='blue', alpha=0.5, pivot='middle', length=0.5)
    ax.quiver(x[~mask], y[~mask], z[~mask], u[~mask], v[~mask], w[~mask], color='gray', alpha=0.5, pivot='middle', length=0.5)
    ax.set_xlabel('z')
    ax.set_ylabel('x')
    ax.set_zlabel('y')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.set_title('Slice Excitation and Selection')

    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])


ani = FuncAnimation(fig, update, frames=60, interval=100)


HTML(ani.to_jshtml())
ani.save('slice_select_3d.gif', writer='pillow', fps=20)
