"""
FlowField initialises a 2d array of Vector objects
and provides methods to lookup and display these vectors.
"""

from p5 import PI, noise, remap, constrain
from p5 import Vector, line, stroke
from p5 import reset_matrix, translate, push_matrix
import copy


class FlowField:
    def __init__(self, vector_strength=1):
        self.resolution = 50
        self.number_of_columns = round(width / self.resolution)
        self.number_of_rows = round(height / self.resolution)
        #  initialize array
        self.field = []
        #  initialise perlin seed
        self.perl_x = 0
        self.perl_y = 0
        self.perl_time = 0
        self.debug = False
        for row in range(self.number_of_rows):
            self.perl_y += 0.05
            self.field.append([])
            for column in range(self.number_of_columns):
                self.perl_x += 0.05
                perlin_2d = noise(self.perl_x, self.perl_y)
                theta = remap(perlin_2d, (0, 1), (0, 2 * PI))
                self.field[row].append(Vector.from_angle(theta) * vector_strength)

    def alter_vectors(self):
        # 3D perlin noise. Z axis is time.
        self.perl_x = 0
        self.perl_y = 0
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                perlin_2d = noise(self.perl_x, self.perl_y, self.perl_time)
                theta = remap(perlin_2d, (0, 1), (0, 2 * PI))
                self.field[row][column].angle = theta
                self.perl_y += 0.01
            self.perl_x += 0.01
        self.perl_time += 0.01

    def display(self):
        stroke(150, 150)
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                origin = [column * self.resolution, row * self.resolution]
                vector_x = copy.copy(self.field[row][column].x)
                vector_y = copy.copy(self.field[row][column].y)
                vector_x *= 10
                vector_y *= 10
                with push_matrix():
                    translate(self.resolution / 2, self.resolution / 2)
                    line((origin), (origin[0] + vector_x, origin[1] + vector_y))
                    reset_matrix()

    def draw_lines(self):
        for col in range(self.number_of_columns):
            line((col * self.resolution, 0), (col * self.resolution, height))
        for row in range(self.number_of_rows):
            line((0, row * self.resolution), (width, row * self.resolution))

    def lookup(self, x, y):
        # Returns a force vector
        # for given location in field
        # specified by pixel position
        column = int(((x / self.resolution) - 0.5))
        row = int(((y / self.resolution) - 0.5))
        column = constrain(column, 0, len(self.field[0]) - 1)
        row = constrain(row, 0, len(self.field) - 1)
        return self.field[row][column]
