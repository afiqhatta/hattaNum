import numpy as np
import math

"""

    def generate_chebyshev(self):
        for i in range(self.size):
            point = math.pi*(2*i - 1)/self.size
            self.xpoints[i] = 0.5*(self.interval[0]+self.interval[1]) + 0.5*(self.interval[1]-self.interval[0])*math.cos(point)

"""

class Data:

    def __init__(self, x_points, y_points, name=None):
        self.x_points = x_points
        self.y_points = y_points
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_points(self):
        for i in range(len(self.x_points)):
            coords = "(" + str(self.x_points[i]) + "," + str(self.y_points[i]) + ")"
            print(coords)

def generate_random(size, interval):
    x_points = np.random.uniform(interval[0], interval[1], size)
    y_points = np.random.uniform(-10, 10, size)
    return Data(x_points, y_points)

a = generate_random(5, [0, 1])
a.get_points()
