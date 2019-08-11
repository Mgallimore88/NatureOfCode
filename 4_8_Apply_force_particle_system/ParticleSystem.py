from Particle import Particle, SquareParticle
from p5 import *
from SurfaceGravity import SurfaceGravity


class ParticleSystem:
    def __init__(self, x, y, identifier=0):
        self.number_of_particles = 1
        self.particles = [0] * self.number_of_particles
        self.identifier = identifier
        self.is_empty = False
        self.origin = Vector(x, y)

        self.width = 100
        self.height = 100
        self.frame_counter = 0
        self.particle_counter = 0
        for n in range(self.number_of_particles):
            self.particles[n] = SquareParticle(self.origin, self.identifier)

    def apply_force(self, force):
        for n in reversed(range(len(self.particles))):
            self.particles[n].applyForce(force)

    def apply_repeller(self, repeller):
        for n in reversed(range(len(self.particles))):
            repel_force = repeller.repel(self.particles[n])
            self.particles[n].applyForce(repel_force)

    def update(self):
        for n in reversed(range(len(self.particles))):
            self.particles[n].display()
            self.particles[n].update()
            self.particles[n].keep_inside_window()

            if self.particles[n].is_dead or self.particles[n].mass == 0:
                self.particles.pop(n)
                # print(f"Particle {n+1} from fountain {self.identifier} died ")

        if len(self.particles) >= 15:
            self.particles.pop(0)

        self.frame_counter += 1
        if self.frame_counter % 10 == 0:
            print(
                f"there are {len(self.particles)} particles in fountain {self.identifier}."
            )
            dice = random_uniform()
            if dice <= 0.4:
                self.particles.append(Particle(self.origin, self.identifier))
            else:
                self.particles.append(SquareParticle(self.origin, self.identifier))
            self.particle_counter += 1
            if self.particle_counter >= 10:
                self.is_empty = True
