import p5

#  sketch to demonstrate what happens if we change the location of the sprite

class Sprite:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.size = 30
    def draw_house(self):
        p5.rect((self.x - self.size/2, self.y), self.size, self.size)
        p5.triangle((self.x-self.size, self.y ), (self.x + self.size, self.y), (self.x, self.y - self.size))
    def draw_pointer(self):
        p5.triangle((self.x,self.y),(self.x-10, self.y+30),(self.x+10, self.y+30))
    def draw_square(self, x=0, y=0):
        p5.rect((self.x, self.y), self.size, self.size)

def setup():
    global sprite_1
    global sprite_2
    p5.size(600, 600)
    sprite_1 = Sprite()
    sprite_2 = Sprite()


def draw():
    global sprite_1
    global sprite_2
    p5.background(255)
    theta = mouse_y
    # sprite_1.x = mouse_x

# reference shape
    sprite_1.draw_pointer()

    p5.fill(255,0,0,128)
#  rotate a house shape about its centre
    with p5.push_matrix():
        p5.translate(40,40)
        p5.rotate(p5.radians(theta))
        sprite_1.draw_house()
    
    p5.fill(250,250,0,127)
    with p5.push_matrix():
        p5.translate(mouse_x, mouse_y)
        p5.rotate(2*p5.PI*mouse_y/height)
        sprite_2.draw_pointer()


p5.run()
