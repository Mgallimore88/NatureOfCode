from p5 import *
from particle_system import *
from vehicle import Vehicle


def setup():
    size(640, 480)
    global brum
    brum = Vehicle()
    

def draw():
    global brum
    background(120)

    brum.update()
    brum.display()
    brum.wraparound()


run()
