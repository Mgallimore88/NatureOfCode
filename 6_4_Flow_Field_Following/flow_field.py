from p5 import *

class FlowField:
    def __init__(self):
        self.resolution = 50
        self.number_of_columns = round(width / self.resolution)
        self.number_of_rows = round(height / self.resolution)
        #  initialize array
        self.field = []
        perlx = 0
        perly = 0
        for row in range(self.number_of_rows):
            perlx += 0.3
            self.field.append([])
            for column in range(self.number_of_columns):
                perly += 0.3
                theta = noise(perlx, perly)
                self.field[row].append(Vector.from_angle(theta))
        print(self.field)

                



    def display(self):
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                with push_matrix():
                    translate(self.resolution/2,self.resolution/2)
                    line((column * self.resolution, row * self.resolution),(self.field[row][column].y * 10 + column * self.resolution, self.field[row][column].x * 10 + row * self.resolution))
                
    def lookup(self, x,y):
        column = int(round(x / self.resolution) - 1)
        row = int(round(y / self.resolution) - 1)
        column = constrain(column, 0, len(self.field[0]) )
        row = constrain(row, 0, len(self.field))

        return self.field[row][column]









    
