from p5 import *
from Mover import *
from wind import *


def setup():
    global movers
    size(640, 480)
    movers = Mover(width, height, 100, 100)


def draw():
    global movers
    background(0)

    movers.update()
    movers.display()
    movers.keep_inside_window()

    if mouse_is_pressed:
        movers.follow(mouse_x, mouse_y)

    if key_is_pressed:
        wind = Wind(mouse_x, mouse_y)
        wind_force = wind.wind_force(movers.location)
        movers.applyForce(wind_force)


run()
