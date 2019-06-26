"""
Raylib has a game controller API that is a bit different from Pygame's
TODO for Richard: Might simplify this a bit more
"""
from richlib import *

alien = Actor('trooper')
alien.size = (20, 20, 20)
alien.pos = (0, 10, 10)


def draw():
    clear()
    alien.draw()


def update():
    if pyray.is_gamepad_available(0):
        if pyray.is_gamepad_button_down(0, rl.GAMEPAD_BUTTON_LEFT_FACE_UP):
            print("up")
        if pyray.is_gamepad_button_down(0, rl.GAMEPAD_BUTTON_RIGHT_FACE_UP):
            print("Y")
        if pyray.get_gamepad_axis_movement(0, rl.GAMEPAD_AXIS_LEFT_X) > 0.3:
            alien.x = alien.x + 1
        elif pyray.get_gamepad_axis_movement(0, rl.GAMEPAD_AXIS_LEFT_X) < -0.3:
            alien.x = alien.x - 1



run()

"""TODO
    make the alien move up/down and forward/back as well as left/right
"""
