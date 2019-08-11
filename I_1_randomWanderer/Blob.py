from RandomWalk import randomWalk
from random import randint
from p5 import circle, constrain


class Blob:
    def __init__(self, width=500, height=500, size=2, stride=2):
        self.width = width
        self.height = height
        self.X = width / 2
        self.Y = height / 2
        self.size = size
        self.stride = 2
        constrain(self.X, 0, self.width - 1)
        constrain(self.Y, 0, self.height - 1)

    def randomWalk(self):
        dice = randint(0, 3)
        if dice == 0:
            self.X -= self.stride
        elif dice == 1:
            self.X += self.stride
        elif dice == 2:
            self.Y -= self.stride
        else:
            self.Y += self.stride

    def render(self):
        circle((self.X, self.Y), self.size)
