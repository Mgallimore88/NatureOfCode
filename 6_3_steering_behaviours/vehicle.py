from p5 import *
import copy


class Vehicle:
    def __init__(self, start_x=width / 2, start_y=height / 2):
        self.location = Vector(start_x, start_y)
        self.velocity = Vector(random_gaussian(2, 3), random_gaussian(2, 3))
        self.mass = 20
        self.acceleration = Vector(0.01, 0.01)
        self.desired_velocity = self.velocity.copy()
        self.max_speed = 4
        self.max_turning = 1

    def moth_steer(self, other):
        self.desired_velocity = other.location - self.location
        self.desired_velocity.normalize
        self.desired_velocity *= self.max_speed
        self.steering_force = self.desired_velocity - self.velocity
        self.steering_force.limit(self.max_turning)
        self.acceleration += self.steering_force

    def seek_and_stop(self, other):
        self.desired_velocity = other.location - self.location
        desired_magnitude = abs(self.desired_velocity.magnitude)
        if desired_magnitude < 100:
            self.arrival_speed = remap(desired_magnitude, (0, 100), (0, self.max_speed))
            print(desired_magnitude)
            self.desired_velocity.normalize
            self.desired_velocity *= self.arrival_speed
        else:
            self.desired_velocity.normalize
            self.desired_velocity *= self.max_speed

        self.steering_force = self.desired_velocity - self.velocity
        self.steering_force.limit(self.max_turning)
        self.acceleration += self.steering_force

    def constant_speed(self, speed=2):
        if mouse_x > 0:
            speed = mouse_x / 100
        self.unit_velocity = copy.copy(self.velocity)
        self.unit_velocity.normalize()
        self.maximized_velocity = self.unit_velocity * speed
        self.constantspeed_force = self.maximized_velocity - self.velocity
        self.acceleration += self.constantspeed_force
        print(self.velocity.magnitude)

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
        line(
            (self.location.x, self.location.y),
            (
                self.location.x + self.velocity.x * 10,
                self.location.y + self.velocity.y * 10,
            ),
        )

    def keep_inside_window(self):
        if 0 >= self.location.x:
            self.location.x = 1
            self.velocity.x *= -1

        elif self.location.x >= width:
            self.location.x = width - 1
            self.velocity.x *= -1

        elif 0 >= self.location.y:
            self.location.y = 1
            self.velocity.y *= -1

        elif self.location.y >= height:
            self.location.y = height - 1
            self.velocity.y *= -1

    def avoid_edges(self):
        if 25 >= self.location.x:
            self.desired_velocity = Vector(self.max_speed, self.velocity.y)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif self.location.x >= width - 25:
            self.desired_velocity = Vector(-self.max_speed, self.velocity.y)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif 25 >= self.location.y:
            self.desired_velocity = Vector(self.velocity.x, self.max_speed)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif self.location.y >= height - 25:
            self.desired_velocity = Vector(self.velocity.x, -self.max_speed)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force
