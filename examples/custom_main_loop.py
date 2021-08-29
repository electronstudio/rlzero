"""
    You can write your own main loop rather than rely on rlzero to magically provide
    one.
"""
from rlzero import *

cube = Cube((0, 10, 0), (10, 20, 10), 'blue')
pyray.set_window_size(800, 500, "title")
camera = pyray.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
pyray.set_camera_mode(camera, pyray.CAMERA_FIRST_PERSON)

while not pyray.window_should_close():

    pyray.update_camera(camera)
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100

    if pyray.is_key_pressed(pyray.KEY_ESCAPE):
        exit()

    pyray.begin_drawing()
    pyray.begin_mode_3d(camera)
    pyray.draw_grid(100, 10)
    clear()
    cube.draw()
    pyray.end_mode_3d()
    pyray.end_drawing()

