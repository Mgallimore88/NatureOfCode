from p5 import *
from Mover import *

def setup():
    global wind
    global gravity
    global movers

    gravity = Vector(0,1.5)
    wind = Vector(0.4,0)
    size(640,480)
    movers = [0] * 4
    for n in range(len(movers)):
        movers[n]=Mover(width,height)

def draw():
    background(0)
    for n in range(len(movers)):
        movers[n].applyForce(gravity*movers[n].mass)
        movers[n].update()
        movers[n].edges()
        movers[n].display()

        if mouse_is_pressed:
            movers[n].applyForce(wind)
        elif key_is_pressed:
            movers[n].applyForce(-wind)

run()