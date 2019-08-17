from p5 import Vector, line
from p5 import random_uniform


class Path:
    def __init__(self):
        self.radius = 20
        self.point_a = Vector(0, height / 4)
        self.point_b = Vector(width, height / 2)

    def update_path(self):
        self.point_a = Vector(0, random_uniform(height))
        self.point_b = Vector(width, random_uniform(height))

    def display(self):
        line(self._tup(self.point_a), self._tup(self.point_b))

    def _tup(self, vec):
        #  takes a vector returns a tuple
        tup = (vec.x, vec.y)
        return tup
