from p5 import *


class Vehicle:
    def __init__(self, start_x=width/2, start_y=height/2):
        self.location = Vector(start_x, start_y)
        self.velocity = Vector(random_gaussian(0, 1), random_gaussian(0, 1))
        self.mass = 20
        self.acceleration = Vector(0.01, 0.01)
        self.desired_velocity = Vector(-1, 0)
        self.max_speed = 0.5
        self.max_turning = 0.5

    def steer(self, other):
        self.desired_velocity = other.location - self.location
        self.desired_velocity.normalize
        self.desired_velocity *= self.max_speed
        self.steering_force = self.desired_velocity - self.velocity
        self.steering_force.limit(self.max_turning)
        self.acceleration += self.steering_force

    def arrive(self, other):
        self.desired_velocity = other.location - self.location
        desired_magnitude = abs(self.desired_velocity.magnitude)
        if desired_magnitude < 100:
            self.arrival_speed = remap(
                desired_magnitude, (0, 100), (0, self.max_speed))
            print(desired_magnitude)
            self.desired_velocity.normalize
            self.desired_velocity *= self.arrival_speed
        else:
            self.desired_velocity.normalize
            self.desired_velocity *= self.max_speed

        self.steering_force = self.desired_velocity - self.velocity
        self.steering_force.limit(self.max_turning)
        self.acceleration += self.steering_force

    def applyForce(self, force):
        self.acceleration += force / self.mass

    def update(self):
        self.location += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0

    def display(self):
        stroke(255)
        fill(255)
        circle((self.location.x, self.location.y), self.mass)
        line((self.location.x, self.location.y), (self.location.x +
                                                  self.velocity.x * 10, self.location.y + self.velocity.y * 10))

    def keep_inside_window(self):
        if 25 >= self.location.x:
            self.steer(Vector(self.velocity.y, -self.velocity.x))
            # self.location.x = 1
            # self.velocity.x *= -1

        elif self.location.x >= width:
            self.location.x = width - 1
            self.velocity.x *= -1

        elif 0 >= self.location.y:
            self.location.y = 1
            self.velocity.y *= -1

        elif self.location.y >= height:
            self.location. y = height-1
            self.velocity.y *= -1
