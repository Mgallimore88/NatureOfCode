from p5 import Vector, line


class Path:
    def __init__(self):
        self.point_a = Vector(0, height/4)
        self.point_b = Vector(width, height/2)
        self.radius = 20

    def display(self):
        line(self._tup(self.point_a), self._tup(self.point_b))

    def _tup(self, vec):
        #  takes a tuple returns a vector
        tup = (vec.x, vec.y)
        return tup


    
