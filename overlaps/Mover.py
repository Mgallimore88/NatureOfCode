from p5 import *


class Mover:
    def __init__(self, width, height):
        self.location = Vector(width - 100, 0)
        self.velocity = Vector(0, 0)
        self.mass = random_uniform(2, 0.1)
        self.acceleration = Vector(0, 0)

    def applyForce(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0

    def display(self):
        stroke(250)
        fill(127)
        circle((self.location.x, self.location.y), self.mass * 20)

    def edges(self):
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
