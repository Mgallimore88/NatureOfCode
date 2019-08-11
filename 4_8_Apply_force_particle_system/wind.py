from p5 import Vector, magnitude, line, stroke


class Wind:
    def __init__(self):
        self.origin = Vector(width / 2, height / 2)

    def wind_force(self, mouse):
        scale = 0.1
        wind_force = self.origin - mouse
        wind_force *= scale
        return wind_force

    def display(self, mouse):
        wind_vector = mouse - self.origin
        stroke(0, wind_vector.magnitude_sq / 1000)
        line(self.origin, mouse)
