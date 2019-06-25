from p5 import *

class Attractor:
    def __init__(self, location , mass):
        self.location = location
        self.mass = mass
        

    def display(self):
        fill(255,255,0)
        circle((self.location),self.mass)

    def attract(self,other):
        bigG = 0.5
        m1 = self.mass
        m2 = other.mass
        r = self.location - other.location
        print(r)
        dSquared = r.magnitude_sq
        print(r)
        #### gravitation
        scalarForce = (bigG * m1 * m2) / dSquared
        constrain(scalarForce, 10, 40 )
        r.normalize
        force = r * scalarForce

        return force


