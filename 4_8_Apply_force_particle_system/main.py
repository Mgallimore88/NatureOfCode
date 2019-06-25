from p5 import *
from ParticleSystem import *
from SurfaceGravity import SurfaceGravity
from wind import Wind
from Attractor import Repeller
def setup():
    size(640,480)
    global fountain
    global gravity
    global wind
    global repeller
    repeller = Repeller(Vector(width/2, height - 100), 40)

    wind = Wind()
    ground = SurfaceGravity()
    gravity = ground.attract()

    initial_num_of_fountains = 1
    fountain = [0] * initial_num_of_fountains
    fountain[0] = ParticleSystem()
def draw():
    global fountain
    global gravity
    global wind
    global repeller

    background(120)
    
    if mouse_is_pressed:
        fountain.append(ParticleSystem(len(fountain)))
        print(f"there are {len(fountain)} fountains.")

    for n in reversed(range(len(fountain))):
        if fountain[n].is_empty:
            print(f"fountain {n} empty")
            fountain.pop(n)
        if mouse_is_pressed and fountain[n].origin.x == 0: # unable to position the initial fountain since mouse_x does not exist yet
            fountain.pop(n)
        fountain[n].run()
        fountain[n].apply_force(gravity)
        fountain[n].apply_repeller(repeller)
        repeller.display()
        if key_is_pressed:
            mouse = Vector(mouse_x, mouse_y)
            fountain[n].apply_force(wind.wind_force(mouse))
            wind.display(mouse)

run()