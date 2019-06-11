from p5 import *

mover = None

class Mover:
    def __init__(self):
        # our object has two Vectors: location and velocity
        self.location = Vector(random_uniform(width),
                               random_uniform(height))

        self.velocity = Vector(random_uniform(low=-2, high=2),
                               random_uniform(low=-2, high=2))

    def update(self):
        # Motion 101: Locations change by velocity
        self.location = self.location + self.velocity

    def display(self):
        stroke(0)
        fill(175)
        circle(self.location, 16)

    def check_edges(self):
        if self.location.x > width:
            self.location.x = 0

        if self.location.x < 0:
            self.location.x = width

        if self.location.y > height:
            self.location.y = 0

        if self.location.y < 0:
            self.location.y = height

def setup():
    global mover
    size(200, 200)
    background(255)

    # make the mover object
    mover = Mover()

def draw():
    no_stroke()
    fill(255, 10)
    rect((0, 0), width, height)

    # call functions on Mover object
    mover.update()
    mover.check_edges()
    mover.display()

if __name__ == '__main__':
    run()