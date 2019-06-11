from p5 import *
from random import randint
from Ball import *


def setup():

    global ball
    size(640, 360)
    no_stroke()
    ball = Ball(width,height)

def draw():
    background(0)
    ball.displayBall()
    ball.checkEdges()

    ball.updateBall()

def key_pressed(event):
    ball.moving = not ball.moving
    print("key_pressed")

run()

