import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

# Define the grid of points where you want to visualize the vector field
x = np.linspace(-5, 5, 15)
y = np.linspace(-5, 5, 15)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()

constant_length_x = 4

frames = []

def update(frame):
    ax.clear()

    condition = (X >= -1) & (X <= 1)

    non_rotating_U = constant_length_x * np.ones_like(X)
    non_rotating_V = np.zeros_like(Y)

    # Calculate phase gradients for rotating vectors in both x and y directions
    phase_gradient_x = (X - X.min()) / (X.max() - X.min()) * 2 * np.pi  # Phase gradient in the x-axis
    phase_gradient_y = (Y - Y.min()) / (Y.max() - Y.min()) * 2 * np.pi  # Phase gradient in the y-axis

    rotation_angle_x = frame * np.pi / 60 + phase_gradient_x  # 60 frames for 180-degree rotation in the x-axis
    rotation_angle_y = frame * np.pi / 60 + phase_gradient_y  # 60 frames for 180-degree rotation in the y-axis

    rotating_U = 4 * np.sin(rotation_angle_x)
    rotating_V = 4 * np.cos(rotation_angle_y)

    U = np.where(condition, rotating_U, non_rotating_U)
    V = np.where(condition, rotating_V, non_rotating_V)

    ax.quiver(X, Y, U, V, color='b', angles='xy', scale_units='xy', scale=10)
    ax.set_xlabel('Z-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Slice Excitation and Phase Encoding')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal')
    ax.grid()

    ax.set_xticks([])
    ax.set_yticks([])

    # Save the current frame as an image
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    frames.append(Image.fromarray(image))

ani = FuncAnimation(fig, update, frames=60, repeat=True, blit=False, interval=50)

# Save the frames as a GIF
ani.save('phase_encoding_gradient.gif', writer='pillow', fps=20)
HTML(ani.to_jshtml())