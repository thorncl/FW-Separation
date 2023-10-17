import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from PIL import Image


x = np.linspace(-5, 5, 15)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()

constant_length_x = 4

frames = []

def update(frame):
    ax.clear()

    condition = (X >= -1) & (X <= 1)

    non_rotating_U = constant_length_x * np.ones_like(X)
    non_rotating_V = np.zeros_like(Y)

    rotating_U = np.zeros_like(X)
    rotating_V = 4 * np.sin(frame * np.pi / 30)

    U = np.where(condition, rotating_U, non_rotating_U)
    V = np.where(condition, rotating_V, non_rotating_V)

    ax.quiver(X[condition], Y[condition], U[condition], V[condition], color='b', angles='xy', scale_units='xy', scale=10)
    ax.quiver(X[~condition], Y[~condition], U[~condition], V[~condition], color='gray', angles='xy', scale_units='xy', scale=10)
    ax.set_xlabel('Z-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Slice Excitation and Selection')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.grid()

    ax.set_xticks([])
    ax.set_yticks([])


    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(Image.fromarray(image))

ani = FuncAnimation(fig, update, frames=60, repeat=True, blit=False, interval=50)


ani.save('slice_select_gradient.gif', writer='pillow', fps=20)
HTML(ani.to_jshtml())