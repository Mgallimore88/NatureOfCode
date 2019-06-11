from p5 import *
from Mover import *

def setup():
    global m
    global wind
    global gravity

    gravity = Vector(0,8)
    wind = Vector(0.5,0)
    size(640,480)
    m=Mover(width,height)

def draw():
    background(0)
    m.applyForce(gravity)
    m.update()
    m.edges()
    m.display()

    if mouse_is_pressed:
        m.applyForce(wind)
    elif key_is_pressed:
        m.applyForce(-wind)

run()