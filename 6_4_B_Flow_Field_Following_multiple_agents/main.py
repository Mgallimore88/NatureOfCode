from p5 import size, background, run, Vector
from particle_system import ParticleSystem
from vehicle import Vehicle
from flow_field import FlowField


def setup():
    size(400, 300)
    global fountain
    global field
    field_strength = 4
    field = FlowField(field_strength)
    fountain = ParticleSystem()


def draw():
    global fountain
    global field
    background(0)

    fountain.run(field)
    field.alter_vectors()

    if key_is_pressed:
        field.display()

run()
