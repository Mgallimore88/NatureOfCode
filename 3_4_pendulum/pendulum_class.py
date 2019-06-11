from p5 import *
from math import sin, cos, pi

class Pendulum:
    def __init__(self, origin, mass, arm_length):
        self.origin = origin
        self.mass = mass
        self.arm_length = arm_length
        self.bob = Vector(self.origin.x, self.arm_length)
        self.angle = pi/4
        self.angular_velocity = 0


    def swing(self, GRAVITY):
        self.bob.x = self.origin.x + self.arm_length * sin(self.angle)
        self.bob.y = self.origin.y + self.arm_length * cos(self.angle)
        self.angular_acceleration = GRAVITY * (50 * self.mass / self.arm_length) * sin(self.angle) 
        self.angle += self.angular_velocity
        self.angular_velocity += self.angular_acceleration
        self.angular_velocity *= 0.99 # Damping

    def display(self):
        line(self.origin, self.bob)
        ellipse((self.bob), self.mass, self.mass)
        





    

