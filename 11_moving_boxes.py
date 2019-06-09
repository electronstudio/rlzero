"""
    to make things move we need to add
    the update() function
"""
from richlib import *

box = Box((0, 10, 0), (10, 20, 10), 'red')

def draw():
    clear()
    box.draw()


def update():
    box.x = box.x + 1
    if box.x > 100:
        box.x = -100

run()

"""TODO
    make box move faster
    move in different direction
    have two boxes with different colours
"""
