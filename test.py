WIDTH=800
HEIGHT=640
CAMERA=rl.CAMERA_FIRST_PERSON
DATA_DIR="examples/models/resources/models/"

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')

def draw():
    clear()
    cube.draw()

def update():
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100
