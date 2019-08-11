from p5 import *
from Orbiter import *
import math


def setup():
    Orbiter.hello()

    size(640, 480)
    background(0)
    global orbiters
    global frame_count
    frame_count = 0
    num_of_orbiters = 10
    orbiters = [Orbiter() for n in range(num_of_orbiters)]


def draw():
    global orbiters
    global frame_count

    translate(width / 2, height / 2)
    background(50)
    frame_count += 1
    for n in range(len(orbiters)):
        orbiters[n].advance(frame_count)
        orbiters[n].display()


run()
