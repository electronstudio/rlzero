"""
    we can check if the mouse pointer is touching a 3d object
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
    if mouse.clicked:
        if mouse.check_collision(cube):
            print("hit")
        else:
            print("miss")

run()

"""TODO
    increase player score every time he clicks on cube
    make cube get smaller each time he clicks on it
    make it move to a random place after it is clicked on, e.g.
        import random
        x = random.randint(0, 100)
"""
