from p5 import Vector


class Wind:
    def __init__(self, mouse_x, mouse_y):
        self.mouse = Vector(mouse_x, mouse_y)

    def wind_force(self, mover):
        scale = 0.001
        wind_force = mover - self.mouse
        wind_force *= scale
        return wind_force
