from p5 import *
from Mover import *


class Fluid:
    def __init__(self, recLeft, recTop, width, height, density):
        self.recLeft = recLeft
        self.recTop = recTop
        self.width = width
        self.recHeight = height / 2
        self.recWidth = width / 2

        self.recRight = self.recLeft + self.recWidth
        self.recBottom = self.recTop + self.recHeight

        self.density = 0.5 if None else density

        # self.drag = Vector(0.1, 0.1)

    def display(self):
        fill(120)
        rect((self.recLeft, self.recTop), self.recWidth, self.recHeight)
        circle((self.recLeft, self.recTop), 30)

    def contains(self, mover):
        if mover.location.x < self.recRight and mover.location.x > self.recLeft:
            if mover.location.y < self.recBottom and mover.location.y > self.recTop:
                return True
        else:
            return False

    def drag(self, mover):  # Does not require the self statement here
        # drag = Vector(0,0)
        drag = mover.velocity.copy()
        # drag = Vector(0,0)
        drag.normalize()
        drag *= -1
        c = 0.01
        drag = drag * c * sq(mag(mover.velocity.x, mover.velocity.y))
        mover.acceleration += drag / mover.mass
        return drag

        # apply force
