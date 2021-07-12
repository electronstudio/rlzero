"""
    to make things move we need to add
    the update() function
"""
from rlzero import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')

def draw():
    clear()
    cube.draw()


def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100

run()

"""TODO
    make box move faster
    make box move in different direction
    make two boxes with different colours
"""

