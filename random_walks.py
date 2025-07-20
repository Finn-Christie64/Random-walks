import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

n = 10000  # Number of steps
x = np.zeros(n)
y = np.zeros(n)
segment_size = 1000

colors_ = np.array(['blue', 'red', 'green', 'orange', 'purple','cyan', 'magenta', 'brown', 'lime', 'pink'])
text_ = np.array(['1,000 is blue \n', '2,000 is red \n', '3,000 is green \n', '4,000 is orange \n', '5,000 is purple \n','6,000 is cyan \n', '7,000 is magenta \n', '8,000 is brown \n', '9,000 is lime \n', '10,000 is pink \n'])  

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

# Side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6)) 

# Static plot
ax1.set_title("Static Path")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_xlim(np.min(x), np.max(x))
ax1.set_ylim(np.min(y), np.max(y))
for i in range(0, n, segment_size):
    end = min(i + segment_size, n)
    color = colors_[(i // segment_size) % len(colors_)]
    ax1.plot(x[i:end], y[i:end], color=color, label=f"{i}-{end}")
ax1.grid()

# Animated plot
ax2.set_xlim(np.min(x), np.max(x))
ax2.set_ylim(np.min(y), np.max(y))
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title("Animated Walk")
ax2.text(1.01, 1, ''.join(text_), transform=ax2.transAxes, fontsize=10, verticalalignment='top', bbox=dict(boxstyle="round", fc="w"))
ax2.grid()

# Setup lines for animation
lines = []
for i in range(0, n, segment_size):
    color = colors_[(i // segment_size) % len(colors_)]
    (l,) = ax2.plot([], [], color=color)
    lines.append(l)

def init():
    for line in lines:
        line.set_data([], [])
    return lines

def update(frame):
    for idx, i in enumerate(range(0, n, segment_size)):
        end = min(i + segment_size, n)
        if frame >= i:
            seg_end = min(frame, end)
            lines[idx].set_data(x[i:seg_end], y[i:seg_end])
    return lines

# Run animation
frame_skip = 2
frames = np.arange(0, n, frame_skip)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=2, repeat=False)

plt.tight_layout()
plt.show()
