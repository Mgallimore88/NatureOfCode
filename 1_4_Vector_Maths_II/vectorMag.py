from p5 import *


def setup():

    global mouse
    global centre

    size(640, 360)
    mouse = Vector(mouse_x, mouse_y)
    centre = Vector(width / 2, height / 2)
    factor = 1


def draw():
    translate(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    mouse -= centre
    m = mouse.magnitude
    background(0)
    fill(255, 255, 0)
    rect((0, -5), m, 10)
    stroke(250)
    line((0, 0), mouse)


def key_pressed(event):

    print("key_pressed ")


run()
