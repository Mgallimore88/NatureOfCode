import copy
import vispy, numpy
from p5 import PI, Vector, line, circle, triangle, fill, stroke, ellipse, remap, TWO_PI
from p5 import (
    random_gaussian,
    random_uniform,
    translate,
    rotate_z,
    push_matrix,
    run,
    Color,
    no_stroke,
)


class Vehicle:
    def __init__(self, start_x=width / 2, start_y=height / 2):
        self.location = Vector(start_x, start_y)
        self.acceleration = Vector(0.01, 0.01)
        self.desired_velocity = Vector(0, 0)
        self.max_speed = 10
        self.max_turning = 0.5
        self.view_range = 100
        centre = Vector(width / 2, height / 2)
        direction = Vector(self.location.x, self.location.y) - centre
        direction.normalize()
        self.velocity = direction * self.max_speed
        self.set_colour()

    def applyForce(self, force):
        self.acceleration += force
        line(
            (self.location.x, self.location.y),
            (self.location.x - force.x, self.location.y - force.y),
        )

    def apply_drag(self, strength=1):
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



    def separate(self, vehicles):
        sum = Vector(0,0)
        count = 0
        for other in vehicles:
            d = Vector.distance(self.location, other.location)
            repel_vector = other.location - self.location
            if d > 0 and d < self.view_range:
                sum += repel_vector
                count += 1
            if count > 0:
                sum /= count
                steering_force = sum - self.velocity
                steering_force.limit(self.max_turning)
                self.applyForce(steering_force)





    def display_circle(self):
        self.set_colour()
        fill(self.colour)
        # no_stroke()
        circle((self.location.x, self.location.y), 15)

    def set_colour(self):
        self.colour = Color(
            remap((self.velocity.angle), (0, TWO_PI), (0, 255)),
            255,
            255,
            color_mode="HSB",
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

    def wraparound(self):
        if 0 >= self.location.x:
            self.location.x = width

        elif self.location.x >= width:
            self.location.x = 1

        elif 0 >= self.location.y:
            self.location.y = height

        elif self.location.y >= height:
            self.location.y = 1

    def _tup(self, vec):
        #  takes a tuple returns a vector
        tup = (vec.x, vec.y)
        return tup
