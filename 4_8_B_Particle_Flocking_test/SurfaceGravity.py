from p5 import Vector, rect, fill
class SurfaceGravity:
    def __init__(self, strength = 12):
        self.strength = strength
    
    def attract(self):
        self. gravity = Vector(0, self.strength)
        return self.gravity
    
    def display(self):
        fill(0,0,250)
        rect((0,height-10),width, height)
        

    
