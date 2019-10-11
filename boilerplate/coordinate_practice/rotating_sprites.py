import p5

#  sketch to demonstrate use of rotation in python mode for processing


class Sprite:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.size = 30

    def draw_house(self):
        p5.rect((self.x - self.size / 2, self.y), self.size, self.size)
        p5.triangle(
            (self.x - self.size, self.y),
            (self.x + self.size, self.y),
            (self.x, self.y - self.size),
        )

    def draw_pointer(self):
        p5.triangle(
            (self.x, self.y), (self.x - 10, self.y + 30), (self.x + 10, self.y + 30)
        )

    def draw_square(self, x=0, y=0):
        p5.rect((self.x, self.y), 40, 40)


def setup():
    global sprite
    p5.size(600, 600)
    sprite = Sprite()


def draw():
    global sprite
    p5.background(255)
    theta = mouse_y

    # reference shape
    sprite.draw_pointer()

    p5.fill(255, 0, 0, 128)
    #  rotate a house shape aboutits centre
    with p5.push_matrix():
        p5.translate(40, 40)
        p5.rotate(p5.radians(theta))
        sprite.draw_house()


p5.run()
