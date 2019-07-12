import p5

class Sprite:
    def __init__(self):
        self.x = 40
        self.y = 40
        self.size = 30
    def draw_house(self):
        p5.rect((self.x - self.size/2, self.y), self.size, self.size)
        p5.triangle((self.x-self.size, self.y ), (self.x + self.size, self.y), (self.x, self.y - self.size))
    def draw_pointer(self):
        p5.triangle((self.x,self.y),(self.x-10, self.y+30),(self.x+10, self.y+30))


def setup():
    global sprite
    p5.size(300, 300)
    sprite = Sprite()
    


def draw():
    global sprite
    p5.background(255)

    sprite.x = mouse_x


#  Draw a red house in start position
    p5.fill(255,0,0,128)
    sprite.draw_house()


    p5.fill(0,255,0,128)
    with p5.push_matrix():

        p5.translate(50,50)
        sprite.draw_house()

        p5.translate(50,50)
        sprite.draw_house()

        p5.translate(50,50)
        sprite.draw_house() 
        # p5.print_matrix()
    p5.fill(0,0,255,128)
    with p5.push_matrix():
        p5.translate(0,50)
        sprite.draw_house()

        p5.translate(0,50)
        sprite.draw_house()

        p5.translate(0,50)
        sprite.draw_house() 

    p5.fill(0,255,255,128)
    with p5.push_matrix():
        sprite.y = mouse_y
        p5.translate(50,0)
        sprite.draw_pointer()

        p5.translate(50,0)
        sprite.draw_pointer()

        p5.translate(50,0)
        sprite.draw_pointer() 
        sprite.y = 20






p5.run()
