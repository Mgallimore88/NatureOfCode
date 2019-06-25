from Particle import Particle, SquareParticle
from verletphysics import *
from p5 import *
from SurfaceGravity import SurfaceGravity

class ParticleSystem:
    def __init__(self, identifier=0):
        self.number_of_particles = 3
        self.particles = [0] * self.number_of_particles
        self.identifier = identifier
        self.is_empty = False
        self.origin = Vector(300, 300)
        self.width = 100
        self.height = 100
        self.counter = 0
        for n in range(self.number_of_particles):
            self.particles[n] = SquareParticle(
                self.origin.x, self.origin.y, self.identifier)

    def apply_force(self, force):
        for n in reversed(range(len(self.particles))):
            self.particles[n].applyForce(force)

    def apply_repeller(self, repeller):
        for n in reversed(range(len(self.particles))):
            repel_force = repeller.repel(self.particles[n])
            self.particles[n].applyForce(repel_force)

    def run(self):
        for n in reversed(range(len(self.particles))):
            self.particles[n].display()
            self.particles[n].update()
            self.particles[n].keep_inside_window()

            if self.particles[n].is_dead or self.particles[n].mass == 0:
                self.particles.pop(n)
                # print(f"Particle {n+1} from fountain {self.identifier} died ")

        if len(self.particles) >= 15:
            self.particles.pop(0)
        if mouse_is_pressed:
            self.origin = Vector(mouse_x, mouse_y)
            self.particles.append(Particle(self.origin.x, self.origin.y, self.identifier))

        