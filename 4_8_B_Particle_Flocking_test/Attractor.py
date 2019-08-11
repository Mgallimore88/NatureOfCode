from p5 import *


class Attractor:
    def __init__(self, location, mass):
        self.location = location
        self.mass = mass

    def display(self):
        fill(255, 255, 0)
        circle((self.location), self.mass)

    def update(self, location):
        self.location = location

    def attract(self, other):
        bigG = 0.5
        m1 = self.mass
        m2 = other.mass
        r = self.location - other.location
        print(r)
        dSquared = r.magnitude_sq
        print(r)
        #### gravitation
        scalarForce = (bigG * m1 * m2) / dSquared
        constrain(scalarForce, 10, 40)
        r.normalize
        force = r * scalarForce
        return force


class Repeller(Attractor):
    def __init__(self, location, mass):
        Attractor.__init__(self, location, mass)

    def repel(self, other):
        bigG = 2
        m1 = self.mass
        m2 = other.mass
        r_attract = self.location - other.location
        r_repel = Vector(r_attract.x * -1, r_attract.y * -1)
        dSquared = r_repel.magnitude_sq
        #### gravitation
        scalarForce = (bigG * m1 * m2) / dSquared
        constrain(scalarForce, 10, 40)
        r_repel.normalize
        force = r_repel * scalarForce
        return force
