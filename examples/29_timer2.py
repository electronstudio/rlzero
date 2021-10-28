from rlzero import *
import random

aliens = []

def add_alien():
    aliens.append(
        Sprite("alien", (random.randint(0,500), random.randint(0,500)))
    )

# call add_alien once, 0.5 seconds from now
schedule_once(add_alien, 0.5)

# call add_alien over and over again, ever 2 seconds
schedule_repeat(add_alien, 2.0)

def draw():
    for alien in aliens:
        alien.draw()

run()