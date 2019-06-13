from p5 import *
from ParticleSystem import *
from wind import *

def setup():
    size(640,480)
    global fountain
    initial_num_of_fountains = 1
    fountain = [0] * initial_num_of_fountains
    fountain[0] = ParticleSystem(width,height)
def draw():
    global fountain

    background(0)
    
    for n in reversed(range(len(fountain))):
        fountain[n].run()
        # if fountain[n].is_empty:
        #     fountain.pop(n)
        if mouse_is_pressed:
            fountain.append(ParticleSystem(width,height, len(fountain)))
        #     print(f"there are {len(fountain)} particle systems.")



run()