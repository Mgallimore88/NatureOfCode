from p5 import *


class Target:
    def __init__(self):
        self.location = Vector(width / 2, height / 4)

    def display(self):
        fill(255, 255, 0)
        circle((self.location.x, self.location.y), 25)

    def follow(self):
        self.location.x = mouse_x
        self.location.y = mouse_y
