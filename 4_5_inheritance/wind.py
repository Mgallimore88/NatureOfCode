from p5 import Vector, magnitude
class Wind:
    def __init__(self, mouse_x, mouse_y):
        self.mouse_position = Vector(mouse_x, mouse_y)
    
    def wind_force(self, particle_position):
        scale = 0.001
        wind_force = (particle_position - self.mouse_position) 
        wind_force *= scale
    
        return wind_force
