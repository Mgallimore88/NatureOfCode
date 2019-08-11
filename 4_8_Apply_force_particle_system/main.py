from p5 import run, background, size, Vector
from ParticleSystem import ParticleSystem
from SurfaceGravity import SurfaceGravity
from wind import Wind
from Attractor import Repeller


def setup():
    size(640, 480)
    global fountains
    global gravity
    global wind
    global repeller
    repeller = Repeller(Vector(width / 2, height - 100), 40)

    wind = Wind()
    ground = SurfaceGravity()
    gravity = ground.attract()

    initial_num_of_fountains = 2
    fountains = []
    for i in range(initial_num_of_fountains):
        fountains.append(ParticleSystem(i * 100, i * 100, i))


def draw():
    global fountains
    global gravity
    global wind
    global repeller

    background(120)

    if mouse_is_pressed:
        fountains.append(ParticleSystem(mouse_x, mouse_y, len(fountains)))
        print(f"there are {len(fountains)} fountains.")

    for fountain in reversed(fountains):

        if fountain.is_empty:
            print(f"fountain {fountain.identifier} empty")
            fountains.remove(fountain)
        fountain.update()
        fountain.apply_force(gravity)
        fountain.apply_repeller(repeller)
        repeller.display()
        if key_is_pressed:
            mouse = Vector(mouse_x, mouse_y)
            fountain.apply_force(wind.wind_force(mouse))
            wind.display(mouse)


run()
