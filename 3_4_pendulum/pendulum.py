from p5 import *
from math import pi
from pendulum_class import *


def setup():
    global swinger

    ARM_LENGTH = 50
    GRAVITY = -0.0003
    MASS = 10
    size(640, 460)
    origin = Vector(width/2, 0)
    
    number_of_swingers = 18
    swinger = [0] * number_of_swingers
    for n in range(len(swinger)):
        swinger[n] = Pendulum(origin, MASS, n/2 * ARM_LENGTH + 1)
        

def draw():
    global swinger
    GRAVITY = -0.0005

    background(0)
    fill(255, 255, 0)
    stroke(250)

    for n in range(len(swinger)):
        swinger[n].swing(GRAVITY)
        swinger[n].display()

def mouse_pressed(event):
    print("mouse_pressed " )
    for n in range(len(swinger)):
        swinger[n].angle =  atan((swinger[n].origin.x - mouse_x) / (swinger[n].origin.y - mouse_y))
        swinger[n].angular_velocity = 0


run()