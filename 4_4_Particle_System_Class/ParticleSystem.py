from Particle import Particle
from wind import Wind
from p5 import *

class ParticleSystem:
    def __init__(self, width = 100, height = 100, identifier = 0):
        self.number_of_particles = 1
        self.particles = [0] * self.number_of_particles
        self.identifier = identifier
        self.is_empty = False
        self.origin = Vector(mouse_x, mouse_y)
        self.width = width 
        self.height = height
        self.counter = 0
        for n in range(self.number_of_particles):
            self.particles[n] = Particle(width,height, self.origin.x, self.origin.y, self.identifier)

    def run(self):
        
        for n in reversed(range(len(self.particles))):
            self.particles[n].display()
            self.particles[n].update()
            self.particles[n].keep_inside_window()

            if key_is_pressed:
                wind = Wind(mouse_x, mouse_y)
                wind_force = wind.wind_force(self.particles[n].location)
                self.particles[n].applyForce(wind_force)

            if self.particles[n].is_dead:
                self.particles.pop(n)
                print(f"Particle {n+1} from fountain {self.identifier} died ")

        if len(self.particles) >=15:
            self.particles.pop(0)
            
        self.counter += 1
        if self.counter % 10 == 0:
            self.particles.append(Particle(self.width,self.height,self.origin.x,self.origin.y, self.identifier))
        
            

            

            # print(f"there are {len(self.particles)} particles.")
            

