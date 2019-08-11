from p5 import *
from Blob import Blob
from RandomWalk import randomWalk


def setup():
    global blob
    size(640, 480)
    background(250)
    no_stroke()
    splat = 3
    stride = 5
    number_of_blobs = 1
    blob = [0] * number_of_blobs
    print(blob)
    for n in range(len(blob)):
        blob[n] = Blob(width, height, splat, stride)


def draw():
    fill(250)
    for i in range(len(blob)):
        blob[i].randomWalk()
        blob[i].render()
    circle((10, 10), 10)


def key_pressed(event):
    background(0)


run()
