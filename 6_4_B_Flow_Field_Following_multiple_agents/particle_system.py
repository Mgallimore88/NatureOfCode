from particle import Particle, SquareParticle
from vehicle import Vehicle
from flow_field import FlowField
from p5 import *


class ParticleSystem:
    def __init__(self, identifier=0, number_of_vehicles=3):
        self.number_of_vehicles = number_of_vehicles
        self.vehicles = []
        self.identifier = identifier
        self.vehicle_identifier = 0
        self.is_empty = False
        self.origin = Vector(mouse_x, mouse_y)
        self.width = 100
        self.height = 100
        self.counter = 0
        for n in range(self.number_of_vehicles):
            self.vehicles.append(
                Vehicle(
                    width * self.vehicle_identifier,
                    self.height * self.vehicle_identifier,
                    self.vehicle_identifier,
                )
            )
            self.vehicle_identifier += 1

    def run(self, field):
        if mouse_is_pressed:
            vehicle_identifier = len(self.vehicles)
            self.vehicles.append(Vehicle(mouse_x, mouse_y, vehicle_identifier))

        for vehicle in reversed(self.vehicles):
            field_force = field.lookup(vehicle.location.x, vehicle.location.y)
            vehicle.apply_force(field_force)
            vehicle.display()
            vehicle.update()
            vehicle.apply_drag()
            vehicle.wraparound()

            if vehicle.is_dead:
                just_died = vehicle.identifier
                self.vehicles.remove(vehicle)
                print(f"Car {just_died} died ")
        # print(f"number of cars = {len(self.vehicles)}")
