"""
    You can write your own main loop rather than rely on rlzero to magically provide
    one.
"""
from rlzero import *

cube = Cube((0, 10, 0), (10, 20, 10), BLUE)
pr.set_window_size(800, 500, "title")
camera = pr.Camera3D([18.0, 16.0, 18.0], [0.0, 0.0, 0.0], [0.0, 1.0, 0.0], 45.0, 0)
pr.set_camera_mode(camera, pr.CAMERA_FIRST_PERSON)

while not pr.window_should_close():

    pr.update_camera(camera)
    cube.x = cube.x + 1
    if cube.x > 100:
        cube.x = -100

    if pr.is_key_pressed(pr.KEY_ESCAPE):
        exit()

    pr.begin_drawing()
    pr.begin_mode_3d(camera)
    pr.draw_grid(100, 10)
    clear()
    cube.draw()
    pr.end_mode_3d()
    pr.end_drawing()

