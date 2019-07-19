from p5 import size, background, run, Vector
from particle_system import ParticleSystem
from vehicle import Vehicle
from flow_field import FlowField


def setup():
    size(400, 300)
    global brum
    global field
    field_strength = 4
    brum = Vehicle()
    field = FlowField(field_strength)

def draw():
    global brum
    global field
    background(120)

    brum.update()
    brum.display()
    field.display()
    # field.draw_lines()
    field.alter_vectors()
    field_force = field.lookup(brum.location.x, brum.location.y)
    brum.applyForce(field_force)
    brum.apply_drag(0.1)
    brum.wraparound()

    brum.spawn_at_mouse_position(mouse_x, mouse_y)
    brum.avoid_zero_velocity()

run()
