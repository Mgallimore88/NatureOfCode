from p5 import *
import math


def setup():
    size(640,480)
    background(0)
    global a
    global r
    global aVel
    global aAcc
    r = 150
    a = 0
    aVel = 0.0
    aAcc = 0.0001

def draw():
    translate(width/2, height/2)
    global a
    global aVel

    a += aVel
    aVel += aAcc

    
    r = 200*sin(a)
    x = r * cos(a)
    y = r * sin(a)
    ellipse((x,y),63, 40)
    line((0,0),(x,y))

def key_pressed(event):
    background(0)

    

run()