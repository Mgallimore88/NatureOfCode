from p5 import *


class Mover:
    def __init__(self, width, height, start_x, start_y):
        self.location = Vector(start_x, start_y)
        self.velocity = Vector(0, 0)
        self.mass = 1.5
        self.acceleration = Vector(0.01, 0.01)

    def applyForce(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.location += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0

    def display(self):
        stroke(250)
        fill(127)
        circle((self.location.x, self.location.y), self.mass * 20)

    def follow(self, mouse_x, mouse_y):
        self.location.x = mouse_x
        self.location.y = mouse_y
        self.velocity *= 0
        self.acceleration *= 0

    def keep_inside_window(self):
        if 0 >= self.location.x:
            self.location.x = 1
            self.velocity.x *= -1

        elif self.location.x >= width:
            self.location.x = width - 1
            self.velocity.x *= -1

        elif 0 >= self.location.y:
            self.location.y = 1
            self.velocity.y *= -1

        elif self.location.y >= height:
            self.location.y = height - 1
            self.velocity.y *= -1
