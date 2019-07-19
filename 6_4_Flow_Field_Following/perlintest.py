from p5 import noise

iterator = 0
xoff = 0

for iterator in range(110):
    xoff += 15
    print(noise(xoff))
