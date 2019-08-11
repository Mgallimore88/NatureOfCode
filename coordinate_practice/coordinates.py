import p5


class Vehicle:
    def __init__(self):
        self.x = 20
        self.y = 20
        self.size = 15


def setup():
    global v
    p5.size(200, 150)
    v = Vehicle()


def draw():
    global v
    p5.background(255)

    #  Draw a rectangle in start position
    p5.fill(192)
    p5.rect((v.x, v.y), v.size, v.size)

    #  Draw a red rectangle in a new position by changing the rect coordianates
    p5.fill(255, 0, 0, 128)
    p5.rect((v.x + 70, v.y + 30), v.size, v.size)

    #  Draw cascading blue rectangles by applying transformations of the canvas
    p5.fill(0, 0, 255, 128)

    p5.push_matrix()
    p5.translate(v.size, v.size)
    p5.rect((v.x, v.y), v.size, v.size)
    p5.translate(v.size, v.size)
    p5.rect((v.x, v.y), v.size, v.size)
    p5.translate(v.size, v.size)
    p5.rect((v.x, v.y), v.size, v.size)

    # reset transformations and reset matrix do the same.

    p5.reset_transforms()

    # an alternative to using push / reset, is the with push:
    p5.fill(0, 255, 0, 128)
    with p5.push_matrix():

        p5.translate(25, 0)
        p5.rect((v.x, v.y), v.size, v.size)

        p5.translate(25, 0)
        p5.rect((v.x, v.y), v.size, v.size)

        p5.translate(25, 0)
        p5.rect((v.x, v.y), v.size, v.size)
        # p5.print_matrix()

    p5.print_matrix()
    print("matrix is back to normal 4x4 numpy ident")


p5.run()
