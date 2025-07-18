import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 10000  # Number of steps
x = np.zeros(n)
y = np.zeros(n)

for i in range(1, n):
    direction = random.randint(1, 4)
    match direction:
        case 1:
            x[i] = x[i - 1] + 1  # Right
            y[i] = y[i - 1]
        case 2:
            x[i] = x[i - 1] - 1  # Left
            y[i] = y[i - 1]
        case 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1  # Up
        case 4:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1  # Down

t = np.arange(n)

# Plot the path
plt.figure()
plt.title(f"2D Random Walk ({n} steps)")
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y)
plt.grid()
plt.show()

#ani
fig, ax = plt.subplots()

ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f"2D Random Walk ({n} steps)")
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

# Animation settings
frame_skip = 1  # Skip steps for performance
frames = np.arange(0, n, frame_skip)

ani = FuncAnimation(
    fig, update, frames=frames, init_func=init,
    blit=True, interval=1, repeat=False
)

plt.grid(True)
plt.show()
