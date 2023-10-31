import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML


fig, ax = plt.subplots()


x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)


quiver = ax.quiver(X, Y, np.ones_like(X), np.zeros_like(Y), angles='xy', scale_units='xy', scale=1, color='b')

def update(frame):

    rotation_speed = (np.abs(X) + 1)/4
    U = np.where(X >= 0, rotation_speed, -rotation_speed) * np.cos(frame * rotation_speed * np.pi / 30)
    V = rotation_speed * np.sin(frame * rotation_speed * np.pi / 30)
    

    vector_length = np.sqrt(U**2 + V**2)
    desired_length = 0.5  
    scaling_factor = desired_length / vector_length
    U *= scaling_factor
    V *= scaling_factor
    
    quiver.set_UVC(U, V)
    return quiver,


ani = FuncAnimation(fig, update, frames=240, repeat=True, blit=False, interval=50)


plt.xlim(-6, 6)
plt.ylim(-6, 6)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title('Frequency Encoding')
plt.show()
ani.save('frequency_encoding_xyplane.gif', writer='pillow', fps=20)
HTML(ani.to_jshtml())