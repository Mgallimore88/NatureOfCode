from p5 import *


def setup():

    global mouse
    global centre
    global factor

    size(640, 360)
    mouse = Vector(mouse_x, mouse_y)
    centre = Vector(width / 2, height / 2)
    factor = 1


def draw():
    translate(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    mouse -= centre
    mouse *= factor
    background(0)
    stroke(250)
    line((0, 0), mouse)


def key_pressed(event):
    global factor
    factor -= 0.05
    round(factor, 1)  # broken
    print("factor = " + str(factor))


run()
