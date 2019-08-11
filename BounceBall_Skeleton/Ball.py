from p5 import *


class Ball:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.moving = True
        self.location = Vector(100, 100)
        self.velocity = Vector(1, 1)
        self.gravity = Vector(0, 0.6)

    def checkEdges(self):
        if 0 >= self.location.x or self.location.x >= self.width:
            self.velocity.x *= -1
        if 0 >= self.location.y or self.location.y >= self.height:
            self.velocity.y *= -1

    def updateBall(self):

        if self.moving == True:
            self.velocity += self.gravity
            self.location = self.location + self.velocity
        else:
            return

    def displayBall(self):
        fill(150, 150, 0)
        circle((self.location.x, self.location.y), 20)
