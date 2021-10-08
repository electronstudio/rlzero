from rlzero import *

WIDTH=800
HEIGHT=640
CAMERA=CAMERA_FIRST_PERSON
DATA_DIR="examples/models/resources/models/"

cube = Cube((0, 10, 0), (10, 20, 10), BLUE)

def draw3d():
    clear()
    cube.draw()

def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100

run()