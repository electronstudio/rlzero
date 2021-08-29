from .util import *
from raylib.pyray import PyRay
from raylib.static import ffi, rl
pyray = PyRay()


class Gamepad:
    """
    Handles input from gamepads
    """
    def __init__(self, id):
        self.id = id

    def test(self):
        if pyray.is_gamepad_available(self.id):
            print("Detected gamepad", self.id, ffi.string(pyray.get_gamepad_name(self.id)))

    @property
    def up(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_LEFT_FACE_UP)

    @property
    def down(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_LEFT_FACE_DOWN)

    @property
    def left(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_LEFT_FACE_LEFT)

    @property
    def right(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_LEFT_FACE_RIGHT)

    @property
    def y(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_RIGHT_FACE_UP)

    @property
    def a(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_RIGHT_FACE_DOWN)

    @property
    def x(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_RIGHT_FACE_LEFT)

    @property
    def b(self):
        return pyray.is_gamepad_button_down(self.id, rl.GAMEPAD_BUTTON_RIGHT_FACE_RIGHT)

    @property
    def left_stick(self):
        return Vector([pyray.get_gamepad_axis_movement(self.id, rl.GAMEPAD_AXIS_LEFT_X),
                       pyray.get_gamepad_axis_movement(self.id, rl.GAMEPAD_AXIS_LEFT_Y)])

    @property
    def right_stick(self):
        return Vector([pyray.get_gamepad_axis_movement(self.id, rl.GAMEPAD_AXIS_RIGHT_X),
                       pyray.get_gamepad_axis_movement(self.id, rl.GAMEPAD_AXIS_RIGHT_Y)])

