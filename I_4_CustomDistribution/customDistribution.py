from p5 import *
from Bar import Bar
from random import randint

def setup():
    background(0)
    global bar
    numberOfBars = 5
    bar = [0] * numberOfBars
    barWidth = width / numberOfBars
    barHeight = 10
    for n in range(numberOfBars):
        bar[n] = Bar(barWidth,height,barHeight,n)

def draw():
    fill(250)
    for n in range(len(bar)):
        bar[n].drawBar()

    n1 = randint(0,len(bar))
    n2 = randint(0,len(bar))
    if n2 < n1:
        bar[n1].grow()
    else:
        return



    
def key_pressed(event):
    background(120)



run()