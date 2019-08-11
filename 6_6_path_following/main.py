from p5 import size, background, run, Vector
import vispy
from vehicle import Vehicle
from path import Path


def setup():
    size(800, 600)
    global mover
    global path
    mover = Vehicle()
    path = Path()


def draw():
    global mover
    global path
    background(120)

    mover.follow(path)
    mover.update()
    mover.display()
    path.display()
    mover.follow(path)
    mover.apply_drag(0.01)
    mover.wraparound()
    mover.spawn_at_mouse_position(mouse_x, mouse_y)

    if mouse_is_pressed:
        path.update_path()



run()
