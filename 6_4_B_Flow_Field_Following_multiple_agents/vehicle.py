from p5 import PI
from p5 import Vector, push_matrix, translate, rotate
from p5 import fill, stroke
from p5 import remap
from p5 import triangle, circle
from p5 import random_gaussian
import copy


class Vehicle:

    def __init__(self, start_x=width/2, start_y=height/2, identifier=0):
        self.location = Vector(start_x, start_y)
        self.initial_velocity = Vector(random_gaussian(2, 3),
                                       random_gaussian(2, 3))
        self.velocity = copy.copy(self.initial_velocity)
        self.desired_velocity = Vector(0, 0)
        self.acceleration = Vector(0.01, 0.01)
        self.max_speed = 1
        self.max_turning = 1
        self.mass = 5
        self.size = 25
        self.initial_lifespan = 100
        self.lifespan = self.initial_lifespan
        self.identifier = identifier
        self.is_dead = False

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

    def check_if_dead(self):
        if self.lifespan <= 0:
            self.is_dead = True
        return self.is_dead

    def apply_force(self, force):
        self.acceleration += force / self.mass

    def apply_drag(self, strength=0.1):
        neg_x = self.velocity.x * -1
        neg_y = self.velocity.y * -1
        drag_vector = Vector(neg_x, neg_y)
        drag_vector.normalize()
        drag_magnitude = self.velocity.magnitude_sq * strength
        drag_force = drag_vector * drag_magnitude
        self.apply_force(drag_force)

    def update(self):
        self.location += self.velocity
        self.velocity += self.acceleration
        self.acceleration *= 0
        self.lifespan -= 1
        self.check_if_dead()

    def display(self):
        colour_scale = remap(self.lifespan, (0, self.initial_lifespan),
                                            (0, 255))
        fill(0, colour_scale, 0, colour_scale)
        stroke(colour_scale, 0, 0, colour_scale)

        theta = self.velocity.angle
        with push_matrix():
            translate(self.location.x, self.location.y)
            rotate(theta + PI/2)
            triangle((0, -self.size/2), 
                     (-self.size/4, self.size/2),
                     (self.size / 4, self.size/2))
        circle((self.location.x, self.location.y), 5)

        """
        display debug vector lines.
        Green = acceleration
        Red = velocity
        """

        # line((self.location.x, self.location.y),
        #      (self.location.x + self.velocity.x * 10,
        #       self.location.y + self.velocity.y * 10))
        # stroke(0, 244, 0)
        # line((self.location.x, self.location.y),
        #      (self.location.x + self.acceleration.x * 100,
        #       self.location.y + self.acceleration.y * 100))

        """ Debug end """

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
            self.velocity = Vector(0, 0)
            self.apply_random_velocity(1)
            self.acceleration = Vector(0, 0)

    def avoid_zero_velocity(self):
        if self.velocity.x == 0 and self.velocity.y == 0:
            self.apply_random_velocity(0.001)

    def apply_random_velocity(self, mean):
        theta = random_uniform(TWO_PI, 0)
        self.velocity = Vector.from_angle(theta)       

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
