"""
    Most of this code is copied from previous programs
"""

from rlzero import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')
DATA_DIR="data"
wiz = Actor('rpg_characters/Wizard')
wiz.size = (20,20,20)
wiz.collision_radius = 20


def draw():
    clear()
    wiz.draw()
    cube.draw()

def update():
    if keyboard.right:
        wiz.x += 1
    elif keyboard.left:
        wiz.x -= 1
    cube.x += 1
    if cube.x > 100:
        cube.x = -100
    if wiz.check_collision(cube):
        wiz.color = RED
    else:
        wiz.color = WHITE

run()

""" TODO
    joystick input (again), vertical movement (again)
    make the box chase the alien
    print number of times hit (the score)
"""
