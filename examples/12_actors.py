"""
    Actors are very similar to cubes!
    The following 3d objects are built-in: barracks, bridge, castle, church, house,
    market, trooper, turret, watermill, well
    If you want any other objects you must provide a .obj file
"""
from richlib import *

alien = Actor('trooper')
alien.size = (20,20,20)


def draw():
    clear()
    alien.draw()


def update():
    alien.x += 1
    if alien.x > 100:
        alien.x = -100

run()

"""TODO
    try some other 3d object build-ins
    try downloading some .obj files from the web
    try creating a .obj file using https://www.leocad.org/ or https://www.blender.org/
"""
