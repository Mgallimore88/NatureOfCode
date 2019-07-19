from p5 import *
import copy


class Vehicle:

    def __init__(self, start_x=width/2, start_y=height/2):
        self.location = Vector(start_x, start_y)
        self.initial_velocity = Vector(random_gaussian(2, 3), random_gaussian(2, 3))
        self.mass = 15
        self.acceleration = Vector(0.01, 0.01)
        self.desired_velocity = Vector(0, 0)
        self.max_speed = 1
        self.max_turning = 1
        self.velocity = copy.copy(self.initial_velocity)

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
        # line((self.location.x,self.location.y), (self.location.x - force.x, self.location.y - force.y))

    def apply_drag(self, strength = 1):
        neg_x = self.velocity.x * -1
        neg_y = self.velocity.y * -1
        drag_vector = Vector(neg_x, neg_y)
        drag_vector.normalize()
        drag_magnitude = self.velocity.magnitude_sq * strength
        drag_force = drag_vector * drag_magnitude
        # print(f"drag_force = {drag_force}")
        self.applyForce(drag_force)


    def update(self):
        self.location += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0


    def display(self):
        stroke(255)
        fill(255)
        theta = self.velocity.angle
        with push_matrix():
            translate(self.location.x, self.location.y)
            rotate_z(theta + PI/2)
            triangle((0, -self.mass/2), (-self.mass/4 ,self.mass/2), (self.mass/4 ,self.mass/2))
        fill(0,255,0)
        circle((self.location.x,self.location.y), 5)

        #debug vector lines

        # line((self.location.x, self.location.y), (self.location.x +
        #                                         self.velocity.x * 10, self.location.y + self.velocity.y * 10))
        # stroke(0,244,0)
        # line((self.location.x, self.location.y), (self.location.x +
        #                                         self.acceleration.x * 500, self.location.y + self.acceleration.y * 500))

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
            self.location. y = height-1
            self.velocity.y *= -1

    def wraparound(self):
        if 0 >= self.location.x:
            self.location.x = width

        elif self.location.x >= width:
            self.location.x = 1

        elif 0 >= self.location.y:
            self.location.y = height

        elif self.location.y >= height:
            self.location. y = 1

    def spawn_at_mouse_position(self, x, y):
        if mouse_is_pressed:
            self.location = Vector(x, y)
            self.velocity = Vector(0,0)
            self.apply_random_velocity(1)
            self.acceleration = Vector(0,0)

    def avoid_zero_velocity(self):
        if self.velocity.x == 0 and self.velocity.y == 0:
            self.apply_random_velocity(0.001)

    def apply_random_velocity(self, mean):
        self.velocity.x += random_gaussian(mean)
        self.velocity.y += random_gaussian(mean)       

    def avoid_edges(self):
        if 25 >= self.location.x:
            self.desired_velocity =Vector(self.max_speed, self.velocity.y)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif self.location.x >= width - 25:
            self.desired_velocity =Vector(-self.max_speed, self.velocity.y)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif 25 >= self.location.y:
            self.desired_velocity =Vector(self.velocity.x, self.max_speed)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force

        elif self.location.y >= height - 25:
            self.desired_velocity =Vector(self.velocity.x, -self.max_speed)

            self.steering_force = self.desired_velocity - self.velocity
            self.steering_force.limit(self.max_turning)
            self.acceleration += self.steering_force
