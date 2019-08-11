from p5 import *
from Ball import *


def setup():

    global mouse
    global centre
    global ball

    size(640, 360)
    mouse = Vector(mouse_x, mouse_y)
    centre = Vector(width / 2, height / 2)
    ball = Ball(width, height)


def draw():
    ball.displayBall()
    ball.moveBall()
    ball.checkEdges()

    translate(width / 2, height / 2)
    mouse = Vector(mouse_x, mouse_y)
    mouse -= centre
    ball.accelerate(mouse / 500)
    m = mouse.magnitude
    background(0)
    fill(255, 255, 0)
    rect((0, -5), m, 10)
    stroke(250)
    line((0, 0), mouse)


def key_pressed(event):

    print("key_pressed ")


run()
