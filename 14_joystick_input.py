"""
Some game controllers have different inputs and some are not be compatible so don'tbe surprised if this doesnt quite work properly!  Use joystick_tester.py to test yours.
"""
from richlib import *

import pygame

joystick = pygame.joystick.Joystick(0)
joystick.init()

alien = Actor('trooper')
alien.size = (20,20,20)
alien.pos = (0, 10, 10)

def draw():
    clear()
    alien.draw()


def update():
    print(joystick.get_axis(0))
    # if pyray.is_gamepad_available(0):
    #     print(pyray.is_gamepad_button_down(0,0))
    #     cd = pyray.get_gamepad_name(0)
        #print(ffi.string(cd))

   # print(pyray.get_gamepad_axis_movement(0, 0))
    if (keyboard.right):
        alien.x = alien.x + 1
    elif (keyboard.left):
        alien.x = alien.x - 1

run()




"""TODO
    make the alien move up and down as well as left and right
"""
