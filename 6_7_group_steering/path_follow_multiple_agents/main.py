from p5 import size, background, run, Vector
import vispy
from particle_system import ParticleSystem
from path import Path


def setup():
    size(80, 60)
    global vehicles
    global path
    vehicles = ParticleSystem()
    path = Path()


def draw():
    global vehicles
    global path
    background(120)
    path.display()

    vehicles.update(path)

    if mouse_is_pressed:
        vehicles.add_one()

    if key_is_pressed:
        path.update_path()
        vehicles.sub_one()


run()
