from Particle import Particle

class SquareParticle(Particle):
    def __init__(self, start_x, start_y, identifier = 0):
        Particle.__init__(self, start_x, start_y, identifier = 0)
    
    def display(self):
        stroke(self.lifespan)
        fill(self.lifespan/2)
        rect((self.location.x,self.location.y),self.mass)