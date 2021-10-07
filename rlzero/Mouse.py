from .util import *
from raylib.pyray import PyRay
from raylib import ffi, rl
import rlzero.globals as Globals
pyray = PyRay()

class Mouse:
    """
    Handles input from mouse
    """
    def get_position_on_ground(self, ground_level):
        pos = pyray.get_mouse_position()
        ray = pyray.get_mouse_ray(pos, Globals.camera[0])
        rayhit = pyray.get_collision_ray_ground(ray, ground_level)
        return Vector([rayhit.position.x, rayhit.position.y, rayhit.position.z])

    @property
    def ground_position(self):
        return self.get_position_on_ground(0)

    @property
    def left_button(self):
        return pyray.is_mouse_button_down(rl.MOUSE_LEFT_BUTTON)

    @property
    def right_button(self):
        return pyray.is_mouse_button_down(rl.MOUSE_RIGHT_BUTTON)

    @property
    def middle_button(self):
        return pyray.is_mouse_button_down(rl.MOUSE_MIDDLE_BUTTON)

    @property
    def clicked(self):
        return pyray.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON)

    def check_collision(self, actor):
        if not actor.loaded:
            actor.load_data()
        pos = pyray.get_mouse_position()
        ray = pyray.get_mouse_ray(pos, Globals.camera[0])
        return pyray.check_collision_ray_box(ray, actor.calc_bounding_box())

