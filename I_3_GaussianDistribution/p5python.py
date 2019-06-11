from p5 import *

def setup():
    size(200,100);
    background(100); 
    # no_stroke()
    # background(10)


def draw():


    if mouse_is_pressed:
        fill(random_uniform(255), random_uniform(127), random_uniform(51), 127)
    else:
        fill(20, 30)

    circle_size = random_uniform(low=10, high=80)

    circle((mouse_x, mouse_y), circle_size)

def key_pressed(event):
    background(204)

run()