from p5 import *


def setup():
    size(500, 500)
    global t
    t = 0


def draw():
    global t
    global ty
    t += 0.05
    ty = t + 20
    x = noise(t)
    y = noise(ty)
    y = remap(y, (0, 1), (0, height))
    x = remap(x, (0, 1), (0, width))
    background(0)
    circle((x, y), 10)


def key_pressed(event):
    background(0)


run()
