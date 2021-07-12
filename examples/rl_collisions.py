"""
    Most of this code is copied from programs 12 and 13
"""

from rlzero import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')
alien = Actor('trooper')
alien.size = (20,20,20)
alien.collision_radius = 20


def draw():
    clear()
    alien.draw()
    cube.draw()

def update():
    if keyboard.right:
        alien.x += 1
    elif keyboard.left:
        alien.x -= 1
    cube.x += 1
    if cube.x > 100:
        cube.x = -100
    if alien.check_collision(cube):
        alien.color = RED
    else:
        alien.color = WHITE

run()

""" TODO
    joystick input (again), vertical movement (again)
    make the box chase the alien
    print number of times hit (the score)
"""
