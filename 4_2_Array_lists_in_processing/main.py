from p5 import *
from Particle import *
from wind import *


def setup():
    global particles
    size(640, 480)

    number_of_particles = 2
    particles = [0] * number_of_particles
    for n in range(number_of_particles):
        particles[n] = Particle(width, height, 100, 100)


def draw():
    global particles
    background(0)

    if len(particles) == 0:  # catch for empty particle list
        particles.append(Particle(width, height, width / 2, height / 2))

    for n in reversed(range(len(particles))):
        particles[n].display()
        particles[n].update()
        particles[n].keep_inside_window()

        if key_is_pressed:
            wind = Wind(mouse_x, mouse_y)
            wind_force = wind.wind_force(particles[n].location)
            particles[n].applyForce(wind_force)

        if particles[n].is_dead:
            particles.pop(n)
            print(f"Particle {n+1} died")

        if len(particles) >= 20:
            particles.pop(0)
            return

        if mouse_is_pressed:
            particles.append(Particle(width, height, 500, 100))
            for m in range(len(particles)):
                particles[m].follow(mouse_x, mouse_y)
            print(f"there are {len(particles)} particles.")
            return


run()
