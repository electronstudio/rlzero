"""
    Actors are very similar to cubes!
"""
from rlzero import *

DATA_DIR="data"

wiz = Actor('rpg_characters/Wizard')
wiz.size = (20,20,20)


def draw():
    clear()
    wiz.draw()


def update():
    wiz.x += 1
    if wiz.x > 100:
        wiz.x = -100

run()

"""TODO
    try some other 3d object build-ins
    try downloading some .glb files from the web
    try creating a .glb file using https://www.leocad.org/ or https://www.blender.org/
"""
