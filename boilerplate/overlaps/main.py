from p5 import *
from Mover import *
from Fluid import *


def setup():
    global wind
    global gravity
    global movers
    global fluid

    gravity = Vector(0, 1.5)
    wind = Vector(0.4, 0)
    size(640, 480)
    movers = [0] * 1
    fluid = Fluid(100, 100, width, height, 0.02)
    for n in range(len(movers)):
        movers[n] = Mover(width, height)


def draw():
    background(0)
    fluid.display()
    for n in range(len(movers)):
        movers[n].applyForce(gravity * movers[n].mass)
        movers[n].update()
        movers[n].edges()
        movers[n].display()

        if fluid.contains(movers[n]):
            background(130)
            print(fluid.drag(movers[n]))

        else:
            background(0)
        #    fluid.applyForce(movers[n])

        if mouse_is_pressed:
            movers[n].applyForce(wind)
        elif key_is_pressed:
            movers[n].applyForce(-wind)


run()
