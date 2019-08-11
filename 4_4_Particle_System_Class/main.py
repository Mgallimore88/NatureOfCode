from p5 import *
from ParticleSystem import *
from wind import *


def setup():
    size(640, 480)
    global fountain
    initial_num_of_fountains = 1
    fountain = [0] * initial_num_of_fountains
    fountain[0] = ParticleSystem(width, height)


def draw():
    global fountain

    background(0)

    if mouse_is_pressed:
        fountain.append(ParticleSystem(width, height, len(fountain)))
        print(f"there are {len(fountain)} fountains.")
    for n in reversed(range(len(fountain))):
        if fountain[n].is_empty:
            print(f"fountain {n} empty")
            fountain.pop(n)
        if (
            mouse_is_pressed and fountain[n].origin.x == 0
        ):  # unable to position the initial fountain since mouse_x does not exist yet
            fountain.pop(n)
        fountain[n].run()


run()
