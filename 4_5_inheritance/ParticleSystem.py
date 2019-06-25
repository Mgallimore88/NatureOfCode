from Particle import Particle, SquareParticle
from p5 import *
from SurfaceGravity import SurfaceGravity

class ParticleSystem:
    def __init__(self, identifier = 0):
        self.number_of_particles = 1
        self.particles = [0] * self.number_of_particles
        self.identifier = identifier
        self.is_empty = False
        self.origin = Vector(mouse_x, mouse_y)
        self.width = 100 
        self.height = 100
        self.counter = 0
        for n in range(self.number_of_particles):
            self.particles[n] = SquareParticle(self.origin.x, self.origin.y, self.identifier)



    def run(self):
        
        for n in reversed(range(len(self.particles))):
            self.particles[n].display()
            self.particles[n].update()
            self.particles[n].keep_inside_window()

            ground = SurfaceGravity()
            ground.display()
            gravity = ground.attract()
            self.particles[n].applyForce(gravity)

            if self.particles[n].is_dead:
                self.particles.pop(n)
                # print(f"Particle {n+1} from fountain {self.identifier} died ")

        if len(self.particles) >=15:
            self.particles.pop(0)
            
        self.counter += 1
        if self.counter % 10 == 0:
            # print(f"there are {len(self.particles)} particles.")
            dice = random_uniform()
            if dice <=0.4:
                self.particles.append(Particle(self.origin.x,self.origin.y, self.identifier))
            else:
                self.particles.append(SquareParticle(self.origin.x,self.origin.y, self.identifier))

        
            

            

            

