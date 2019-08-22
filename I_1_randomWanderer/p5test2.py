from p5 import (
    no_stroke,
    background,
    fill,
    size,
    run,
    fill,
    noise,
    random_uniform,
    circle,
    remap,
    rect,
)


def setup():
    size(640, 360)
    no_stroke()
    background(0)
    global perlx
    global perly
    perlx = random_uniform(1000)
    perly = 0


def draw():
    global perlx
    global perly

    perlx += 0.005
    perly += 0.005
    fill(remap(noise(perlx), (0, 1), (0, 255)), (255), (255), 100, color_mode="HSB")

    rect((width - 10, height), 10, -10, mode="CORNER")

    if mouse_is_pressed:
        fill(remap(noise(perlx), (0, 1), (0, 255)), (255), (255), 100, color_mode="HSB")
    else:
        fill(255, 15)

    circle_size = 25 * (noise(perlx, perly) + 1)

    circle((mouse_x, mouse_y), circle_size)


def key_pressed(event):
    global recording
    background(0)


run()
