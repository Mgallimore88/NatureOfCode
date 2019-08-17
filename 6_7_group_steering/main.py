from p5 import size, background, run, Vector
import vispy, numpy
from particle_system import ParticleSystem


def setup():
    size(700, 700)
    global vehicles
    vehicles = ParticleSystem()


def draw():
    global vehicles
    background(0)
    vehicles.update()

    if mouse_is_pressed:
        vehicles.add_one()

    if key_is_pressed:
        vehicles.sub_one()


run()
