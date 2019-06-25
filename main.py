# Author: Artur Szcześniak
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


INTERVAL = 0

def get_random_point():
    x, y = random.uniform(-1, 1), random.uniform(-1, 1)
    return x, y


def point_is_in_circle(point, radius):
    if point[0] ** 2 + point[1] ** 2 < radius ** 2:
        return True
    else:
        return False


fig, ax = plt.subplots(num="Monte Carlo PI")
fig.set_size_inches(9, 9)
ax.set_facecolor((0.1, 0.1, 0.1))
# circle = plt.Circle((0, 0), 1, fill=False, edgecolor=(0.8, 0.9, 0.8))
# ax.add_artist(circle)
inside_scatter = plt.scatter([], [])
outside_scatter = plt.scatter([], [])
in_points = []
out_points = []


def add_point(frame):
    point = get_random_point()
    if point_is_in_circle(point, 1):
        in_points.append(point)
    else:
        out_points.append(point)
    x_in_vect = [point[0] for point in in_points]
    y_in_vect = [point[1] for point in in_points]
    x_out_vect = [point[0] for point in out_points]
    y_out_vect = [point[1] for point in out_points]
    inside_scatter = plt.scatter(x_in_vect,
                                 y_in_vect,
                                 c=[[0.9, 0.9, 0.9]],
                                 s=2)
    outside_scatter = plt.scatter(x_out_vect,
                                  y_out_vect,
                                  c=[[0.4, 0.2, 0.2]],
                                  s=2)
    try:
        pi = 4 * len(in_points) / frame
    except ZeroDivisionError:
        pi = 0
    pitext = plt.text(-0.97, -0.96,
                      "Calculated pi: {:1.5f}".format(pi),
                      bbox={'facecolor': 'w', 'alpha': 0.99, 'pad': 5})
    itertext = plt.text(-0.97, -0.88,
                        "Iterations: {}".format(frame),
                        bbox={'facecolor': 'w', 'alpha': 0.99, 'pad': 5})
    return inside_scatter, outside_scatter, itertext, pitext


def init():
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    return inside_scatter, outside_scatter


ani = animation.FuncAnimation(fig, add_point, init_func=init, interval=INTERVAL, blit=True)
plt.show()
