from p5 import *
from Mover import *
from Attractor import *

def setup():
    global wind
    global gravity
    global movers
    global sun
    
    sun = Attractor((Vector(300,300)),50)
    #gravity = Vector(0,1.5)
    wind = Vector(0.4,0)

    size(640,480)
    movers = [0] * 6
    for n in range(len(movers)):
        movers[n]=Mover(width,height)

def draw():
    background(0)
    sun.display()
    for n in range(len(movers)):
        #movers[n].applyForce(gravity*movers[n].mass)
        f = sun.attract(movers[n])
        movers[n].applyForce(f)
        movers[n].update()
        # movers[n].edges()
        movers[n].display()




        if mouse_is_pressed:
            sun.location.x = mouse_x
            sun.location.y = mouse_y

        elif key_is_pressed:
            movers[n].applyForce(-wind)

run()