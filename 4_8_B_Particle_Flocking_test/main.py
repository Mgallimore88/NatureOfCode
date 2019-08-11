from p5 import *
from ParticleSystem import *
from SurfaceGravity import SurfaceGravity
from wind import Wind
from Attractor import Repeller


def setup():
    size(640, 480)
    global fountain
    global gravity
    global wind
    global repeller
    repeller = Repeller(Vector(width / 2, height - 100), 40)

    wind = Wind()
    ground = SurfaceGravity()
    gravity = ground.attract()

    initial_num_of_fountains = 1
    fountain = [0] * initial_num_of_fountains
    fountain[0] = ParticleSystem()


def draw():

    global fountain
    background(120)
    fountain[0].run()


run()
