from p5 import *
from Particle import *
from wind import *

def setup():
    global particles
    size(640,480)

    number_of_particles = 1
    particles = [0] * number_of_particles
    for n in range(number_of_particles):
        particles[n] = Particle(width,height, 100, 100)

def draw():
    global particles
    background(0)

    for n in range(len(particles)):
        particles[n].update()
        particles[n].display()
        particles[n].keep_inside_window()

        if mouse_is_pressed:
            particles[n].follow(mouse_x, mouse_y)
            particles.append(Particle(width,height,100,100))
            print(f"there are {len(particles)} particles.")

        if key_is_pressed:
            wind = Wind(mouse_x, mouse_y)
            wind_force = wind.wind_force(particles[n].location)
            particles[n].applyForce(wind_force)

        if len(particles) >=19:
            particles.pop()
    

        


        

run()