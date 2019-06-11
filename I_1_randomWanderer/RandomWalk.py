from random import randint

def randomWalk(blob):
    dice = randint(0,3)
    if dice == 0:
        blob.X -= blob.stride
    elif dice == 1:
        blob.X += blob.stride
    elif dice == 2:
        blob.Y -= blob.stride
    else:
        blob.Y += blob.stride
    

