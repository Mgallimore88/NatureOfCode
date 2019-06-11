#Normal distribution example.
#Press keyboard to increase sigma. 

from p5 import *

from random import *

def setup():
    background(0)
    global mu
    global sigma
    mu = width/2      #mean
    sigma = 2   #sd
   

def draw():
    global sigma
    x = normalvariate(mu, sigma)
    y = normalvariate(height/2, 10)
    
    no_stroke()
    fill(20,250,250, 10)

    circle((x,y), normalvariate(10,10))

def key_pressed(event):
    global sigma
    sigma = sigma *1.1

run()