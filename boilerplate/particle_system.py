from vehicle import Vehicle
from p5 import Vector


class ParticleSystem:
    def __init__(self):
        self.num_of_vehs = 1
        self.origin = Vector(width / 2, height / 2)
        self.vehicles = [Vehicle()] * self.num_of_vehs
        self.debug = False

    def apply_force(self, force):
        for vehicle in self.vehicles:
            vehicle.applyForce(force)

    def update(self, path):
        for vehicle in reversed(self.vehicles):
            vehicle.display()
            vehicle.update()
            vehicle.follow(path)
            vehicle.follow(path)
            vehicle.apply_drag(0.01)
            vehicle.wraparound()

    def add_one(self):
        self.vehicles.append(Vehicle(mouse_x, mouse_y))

    def sub_one(self):
        if len(self.vehicles):
            self.vehicles.pop(0)

        if self.debug:
            self.frame_counter += 1
            if self.frame_counter % 10 == 0:
                print(
                    f"there are {len(self.vehicles)} vehicles in fountain {self.identifier}."
                )
                dice = random_uniform()
                if dice <= 0.4:
                    self.vehicles.append(vehicle(self.origin, self.identifier))
                else:
                    self.vehicles.append(Squarevehicle(self.origin, self.identifier))
                self.vehicle_counter += 1
                if self.vehicle_counter >= 10:
                    self.is_empty = True
