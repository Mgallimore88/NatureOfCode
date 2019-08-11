import random
from p5 import *


class Orbiter:
    """ define an orbiter """

    @classmethod
    def hello(cls):
        print("Hello")

    def __init__(self):
        self.x_period = random_uniform(50, 150)
        self.y_period = random_uniform(50, 150)
        self.x_amplitude = random_uniform(100, 200)
        self.y_amplitude = random_uniform(100, 200)

    def advance(self, frame_count):
        self.frame_count = frame_count
        self.x = self.x_amplitude * sin(self.frame_count * TWO_PI / self.x_period)
        self.y = self.y_amplitude * cos(self.frame_count * TWO_PI / self.y_period)

    def display(self):
        stroke(250)
        ellipse((self.x, self.y), 30, 30)
        line((0, 0), (self.x, self.y))
