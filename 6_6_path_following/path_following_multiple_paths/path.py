from p5 import Vector, line
from p5 import random_uniform
from p5 import *


class Path:
    def __init__(self, num_of_paths=4):
        self.num_of_paths = num_of_paths
        self.radius = 5
        self.first_point = Vector(0, random_uniform(height, 0))
        self.points = []

    def populate(self):
        self.points = []
        self.points.append(self.first_point)
        for point in range(self.num_of_paths):
            self.points.append(
                Vector(
                    ((point + 1) * width / self.num_of_paths), random_uniform(height, 0)
                )
            )

    def add_point(self, point):  # takes a Vector
        self.points.append(point)

    def display(self):
        for i in range(len(self.points) - 1):

            line(self._tup(self.points[i]), self._tup(self.points[i + 1]))

        # line(self._tup(self.point_a), self._tup(self.point_b))

    def _tup(self, vec):
        #  takes a vector returns a tuple
        tup = (vec.x, vec.y)
        return tup
