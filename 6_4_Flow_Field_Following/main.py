from p5 import *
from particle_system import *
from vehicle import Vehicle
from flow_field import FlowField


def setup():
    size(400, 200)
    global brum
    global field
    brum = Vehicle()
    field = FlowField()

def draw():
    global brum
    global field
    background(120)

    field.display()


    brum.update()
    brum.applyForce(field.lookup(brum.location.x,brum.location.y))
    brum.display()
    brum.wraparound()


run()
