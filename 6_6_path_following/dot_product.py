from p5 import size, background, line, Vector, run
from p5 import *

def dot_product(vector1, vector2):
    dp = (vector1.x * vector2.x 
          + vector1.y * vector2.y)
    return dp

def scalar_projection(p, a, b):
    ap = p - a
    ab = b - a
    ab.normalize()
    dp = float(ap.dot(ab))
    print(dp)
    ab *= dp
    normal_point = a + ab
    return normal_point

def setup():
    global point_a
    global point_b
    size(600, 360)
    background(255)
    point_a = Vector(100, 300)
    point_b = Vector(400, 100)

def draw():
    background(250)
    global point_a
    global point_b
    stroke(0)
    mouseX = mouse_x
    mouseY = mouse_y
    mouse = Vector(mouseX, mouseY)
    mouse_point = Vector(mouse_x, mouse_y)
    
    line(point_a, mouse)
    line(point_a, point_b)

    norm = scalar_projection(mouse, point_a, point_b)
    ellipse((norm.x, norm.y), 10, 10)

run()
