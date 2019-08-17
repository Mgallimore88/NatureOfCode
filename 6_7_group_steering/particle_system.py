from vehicle import Vehicle
from p5 import Vector, random_uniform
import vispy, numpy


class ParticleSystem:
    def __init__(self):
        self.num_of_vehs = 10
        self.vehicles = []
        for i in range(self.num_of_vehs):
            self.vehicles.append(Vehicle(random_uniform(width), random_uniform(height)))
        self.debug = False

    def apply_force(self, force):
        for vehicle in self.vehicles:
            vehicle.applyForce(force)

    def update(self):
        for vehicle in reversed(self.vehicles):
            vehicle.display_circle()
            vehicle.update()
            vehicle.align(self.vehicles, "max")
            vehicle.wraparound()

    def add_one(self):
        self.vehicles.append(Vehicle(mouse_x, mouse_y))

    def sub_one(self):
        if len(self.vehicles) > 0:
            self.vehicles.pop(0)
