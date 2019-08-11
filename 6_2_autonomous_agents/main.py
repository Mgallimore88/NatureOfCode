from p5 import *
from particle_system import *
from target import Target
from vehicle import Vehicle


def setup():
    size(640, 480)
    global target
    global brum
    brum = Vehicle()
    target = Target()


def draw():
    global target
    global brum
    background(120)
    target.display()

    brum.constant_speed()
    brum.keep_inside_window()
    brum.update()
    brum.display()
    brum.moth_steer(target)

    if mouse_is_pressed:
        target.follow()


run()
