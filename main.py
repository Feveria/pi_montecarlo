# Author: Artur Szcześniak
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

POINTS = 100000
INTERVAL = 1


def get_random_point():
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    return x, y


def point_is_in_circle(point, radius):
    if point[0] ** 2 + point[1] ** 2 < radius ** 2:
        return True
    else:
        return False


def add_point(_):
    point = get_random_point()
    if point_is_in_circle(point, 1):
        color = 'red'
    else:
        color = 'blue'
    sctr = plt.scatter(*point, s=8, c=color)
    return sctr,


fig = plt.figure()
fig.set_size_inches(9, 9)
plt.axis([-1, 1, -1, 1])

anim = animation.FuncAnimation(fig, add_point,  interval=INTERVAL, blit=False)
plt.show()
