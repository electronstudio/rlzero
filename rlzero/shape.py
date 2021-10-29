from raylib import ffi, rl
from raylib.colors import *
from .common import _gen_file_paths, find_file
from .util import *
import rlzero.globals as Globals
import os

import pyray as pr


class Shape:
    """
    Abstract base class for all 3d objects.
    """

    @property
    def color(self):
        """
        Base Color of the object.
        """
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def pos(self):
        """
        Position Vector in 3d space.
        """
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = Vector(value)

    @property
    def wire_color(self):
        """
        If drawing wireframe, use this Color.
        """
        return self._wire_color

    @wire_color.setter
    def wire_color(self, value):
        self._wire_color = Color(value)

    @property
    def x(self):
        """
        Shortcut to the x co-ordinate float of the object position
        """
        return self.pos.x

    @x.setter
    def x(self, value):
        self.pos.x = value

    @property
    def y(self):
        """
       Shortcut to the y co-ordinate float of the object position
       """
        return self.pos.y

    @y.setter
    def y(self, value):
        self.pos.y = value

    @property
    def z(self):
        """
       Shortcut to the z co-ordinate float of the object position
       """
        return self.pos.z

    @z.setter
    def z(self, value):
        self.pos.z = value


# class Box(Shape):
#     def __init__(self, position, scale, color=RED, wires=True, wire_color=DARKGRAY):
#         self.pos = position
#         self.scale = scale
#         self.color = color
#         self.wire_color = wire_color
#         self.wires = wires
#
#     # def __getattr__(self, item):
#     #     return self.pos.item
#     #
#     # def __setattr__(self, key, value):
#     #     self.pos.key = value
#
#     @property
#     def scale(self):
#         return self._scale
#
#     @scale.setter
#     def scale(self, value):
#         print("setting scale ", value, type(value))
#         self._scale = Vector(value)
#
#     def get_bounding_box(self):
#         return (
#             (
#                 self.pos.x - self.scale.x / 2,
#                 self.pos.y - self.scale.y / 2,
#                 self.pos.z - self.scale.z / 2,
#             ),
#             (
#                 self.pos.x + self.scale.x / 2,
#                 self.pos.y + self.scale.y / 2,
#                 self.pos.z + self.scale.z / 2,
#             )
#         )
#
#     def draw(self):
#         #print("draw color ",self.color)
#         rl.DrawCubeV(self.pos, self.scale, self.color)
#         if self.wires:
#             rl.DrawCubeWiresV(
#                 self.pos, self.scale, self.wire_color
#             )
#
#     def check_collision(self, other):
#         if isinstance(other, Sphere):
#             r = rl.CheckCollisionBoxSphere(
#                 self.get_bounding_box(), other.pos, other.radius
#             )
#             return r
#         elif isinstance(other, Box):
#             return rl.CheckCollisionBoxes(self.get_bounding_box(), other.get_bounding_box())
#         elif isinstance(other, Model):
#             return self.check_collision(other.collision_sphere)


# class Sphere(Shape):
#     def __init__(self, position, radius, color=RED, wires=True, wire_color=DARKGRAY):
#         self.pos = position
#         self.radius = radius
#         self.color = color
#         self.wire_color = wire_color
#         self.wires = wires
#
#     def draw(self):
#         rl.DrawSphere(self.pos, self.radius, self.color)
#         if self.wires:
#             rl.DrawSphereWires(self.pos, self.radius, 32, 32, self.wire_color)
#
#     def check_collision(self, other):
#         if isinstance(other, Sphere):
#             return rl.CheckCollisionSpheres(
#                 self.pos, self.radius, other.pos, other.radius
#             )
#         elif isinstance(other, Box):
#             return rl.CheckCollisionBoxSphere(
#                 other.get_bounding_box(), self.pos, self.radius
#             )
#         elif isinstance(other, Model):
#             return self.check_collision(other.collision_sphere)


