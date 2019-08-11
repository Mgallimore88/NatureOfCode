from p5 import *


class Ball:
    # All methods defined in a class in Python require (self) as the first parameter.
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.moving = True
        self.location = Vector(100, 100)
        self.velocity = Vector(1, 1)
        self.accelX = 1.1
        self.accelY = 1.1

    def displayBall(self):
        fill(150, 150, 0)
        circle((self.location.x, self.location.y), 20)

    def moveBall(self):

        if self.moving == True:
            self.location = self.location + self.velocity
        else:
            return

    def checkEdges(self):
        if 0 >= self.location.x or self.location.x >= self.width:
            self.velocity.x *= -self.accelX
        if 0 >= self.location.y or self.location.y >= self.height:
            self.velocity.y *= -self.accelY
