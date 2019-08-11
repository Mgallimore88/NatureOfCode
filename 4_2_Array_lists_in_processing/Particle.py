from p5 import *


class Particle:
    def __init__(self, width, height, start_x, start_y):
        self.location = Vector(start_x, start_y)
        self.velocity = Vector(random_gaussian(0, 1), random_gaussian(0, 1))
        self.mass = 0.4
        self.acceleration = Vector(0.01, 0.01)
        self.is_dead = False

    def applyForce(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.location += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0

    def display(self):
        no_stroke()
        fill(
            self.mass * 200,
            self.acceleration.magnitude_sq * 500,
            self.velocity.magnitude_sq * 20,
        )
        circle((self.location.x, self.location.y), self.mass * 20)

    def follow(self, mouse_x, mouse_y):
        self.location.x = mouse_x
        self.location.y = mouse_y
        self.velocity = Vector(random_gaussian(0, 1), random_gaussian(0, 1))
        self.acceleration *= 0
        self.mass = mouse_x / 300

    def keep_inside_window(self):
        if 0 >= self.location.x:
            self.location.x = 1
            self.velocity.x *= -1

        elif self.location.x >= width:
            self.location.x = width - 1
            self.velocity.x *= -1

        elif 0 >= self.location.y:
            self.is_dead = True
            return
            # self.location.y = 1
            # self.velocity.y *= -1

        elif self.location.y >= height:
            self.location.y = height - 1
            self.velocity.y *= -1
