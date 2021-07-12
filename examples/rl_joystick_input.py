"""
Richlib has a gamepad API that is a bit different from Pygame's
"""
from rlzero import *

alien = Actor('trooper')
alien.size = (20, 20, 20)
alien.pos = (0, 10, 10)


def draw():
    clear()
    alien.draw()


def update():
    if gamepad.up:
        print("up")
    if gamepad.y:
        print("Y")
    if gamepad.left_stick.x > 0.3:
        alien.x = alien.x + 1
    elif gamepad.left_stick.x < -0.3:
        alien.x = alien.x - 1


run()

"""TODO
    make the alien move up/down and forward/back as well as left/right
"""
