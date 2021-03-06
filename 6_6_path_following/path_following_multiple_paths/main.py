from p5 import size, background, run, Vector
import vispy
from particle_system import ParticleSystem
from path import Path


def setup():
    size(800, 600)
    global vehicles
    global path
    vehicles = ParticleSystem()
    path = Path()
    path.populate()


def draw():
    global vehicles
    global path
    background(120)
    path.display()

    vehicles.update(path)

    if mouse_is_pressed:
        vehicles.add_one()

    if key_is_pressed:
        # vehicles.sub_one()
        path.populate()


run()
