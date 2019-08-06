from p5 import size, background, run, Vector
from vehicle import Vehicle
from path import Path

def setup():
    size(400, 300)
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
    # mover.follow(path)
    # mover.apply_drag(0.1)
    mover.wraparound()

    mover.spawn_at_mouse_position(mouse_x, mouse_y)
    mover.avoid_zero_velocity()

run()
