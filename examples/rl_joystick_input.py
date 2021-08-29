"""
RLZero has a gamepad API that is a bit different from Pygame's
"""
from rlzero import *

DATA_DIR="data"

wiz = Actor('rpg_characters/Wizard')
wiz.size = (20, 20, 20)
wiz.pos = (0, 10, 10)


def draw():
    clear()
    wiz.draw()


def update():
    if gamepad.up:
        print("up")
    if gamepad.y:
        print("Y")
    if gamepad.left_stick.x > 0.3:
        wiz.x = wiz.x + 1
    elif gamepad.left_stick.x < -0.3:
        wiz.x = wiz.x - 1


run()

"""TODO
    make the wiz move up/down and forward/back as well as left/right
"""
