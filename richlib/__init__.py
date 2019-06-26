""" Richlib, simple access to Raylib
"""
__version__ = '0.1'

from raylib.static import ffi, rl
# from ..dynamic import ffi, raylib as rl
from raylib.colors import *
from .util import *

import sys
import os
from .rlights import *

data_dir = ""

from raylib.pyray import PyRay

pyray = PyRay()
screen = pyray

camera = ffi.new("struct Camera3D *")
camera.position = (0.0, 100, 100)
camera.target = (0.0, 0.0, 0.0)
camera.up = (0, 1, 0)
camera.fovy = 45
camera.type = rl.CAMERA_PERSPECTIVE

mod = sys.modules['__main__']


def clear(color=RAYWHITE):
    rl.ClearBackground(Color(color))


class Shape:
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = Color(value)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = Vector(value)

    @property
    def wire_color(self):
        return self._wire_color

    @wire_color.setter
    def wire_color(self, value):
        self._wire_color = Color(value)

    @property
    def x(self):
        return self.pos.x

    @x.setter
    def x(self, value):
        self.pos.x = value

    @property
    def y(self):
        return self.pos.y

    @y.setter
    def y(self, value):
        self.pos.y = value

    @property
    def z(self):
        return self.pos.z

    @z.setter
    def z(self, value):
        self.pos.z = value


# class Box(Shape):
#     def __init__(self, position, size, color=RED, wires=True, wire_color=DARKGRAY):
#         self.pos = position
#         self.size = size
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
#     def size(self):
#         return self._size
#
#     @size.setter
#     def size(self, value):
#         print("setting size ", value, type(value))
#         self._size = Vector(value)
#
#     def get_bounding_box(self):
#         return (
#             (
#                 self.pos.x - self.size.x / 2,
#                 self.pos.y - self.size.y / 2,
#                 self.pos.z - self.size.z / 2,
#             ),
#             (
#                 self.pos.x + self.size.x / 2,
#                 self.pos.y + self.size.y / 2,
#                 self.pos.z + self.size.z / 2,
#             )
#         )
#
#     def draw(self):
#         #print("draw color ",self.color)
#         rl.DrawCubeV(self.pos, self.size, self.color)
#         if self.wires:
#             rl.DrawCubeWiresV(
#                 self.pos, self.size, self.wire_color
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
#         elif isinstance(other, Actor):
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
#         elif isinstance(other, Actor):
#             return self.check_collision(other.collision_sphere)


class Actor(Shape):
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = Vector(value)

    def __init__(self, model_file, position=(0, 0, 0), collision_radius=0, texture_file="",
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0, size=(1, 1, 1), color=WHITE, wires=False,
                 wire_color=DARKGRAY):
        # super().__init__(position, collision_radius, color, wires, wire_color)

        self.pos = position
        self.color = color
        self.wire_color = wire_color
        self.wires = wires

        self.model_file = model_file
        if texture_file == "":
            texture_file = model_file + "_diffuse"
        self.texture_file = texture_file
        self.size = size
        self.rotation_axis = rotation_axis
        self.rotation_angle = rotation_angle
        self.collision_radius = collision_radius
        self.loaded = False

    def load_data(self):
        self.loaded = True
        print("*** DATA_DIR=", data_dir)
        file = data_dir + self.model_file + '.obj'
        if not os.path.isfile(file):
            file = str(PATH / 'models' / self.model_file) + '.obj'
        if not os.path.isfile(file):
            raise Exception(f"file {self.model_file} does not exist")


        self.model = rl.LoadModel(file.encode('utf-8'))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat

        tfile = data_dir + self.texture_file + '.png'
        if not os.path.isfile(tfile):
            tfile = str(PATH / 'models' / self.texture_file) + '.png'

        texture = rl.LoadTexture(tfile.encode('utf-8'))
        if texture.format:
            self.model.materials[0].maps[rl.MAP_DIFFUSE].texture = texture


        self.model.materials[0].shader = lightSystem.shader
        self.bounding_box = self.calc_bounding_box()

    def calc_bounding_box(self):
        if not hasattr(self, 'model'):
            return ((0, 0, 0), (0, 0, 0))
        bb = rl.MeshBoundingBox(self.model.meshes[0])

        bb.min.x *= self.size.x
        bb.min.y *= self.size.y
        bb.min.z *= self.size.z
        bb.max.x *= self.size.x
        bb.max.y *= self.size.y
        bb.max.z *= self.size.z

        bb.min.x += self.pos.x
        bb.min.y += self.pos.y
        bb.min.z += self.pos.z
        bb.max.x += self.pos.x
        bb.max.y += self.pos.y
        bb.max.z += self.pos.z
        return bb

    def calc_centre(self):
        centre_x = (self.bounding_box.max.x + self.bounding_box.min.x) / 2
        centre_y = (self.bounding_box.max.y + self.bounding_box.min.y) / 2
        centre_z = (self.bounding_box.max.z + self.bounding_box.min.z) / 2
        return (centre_x, centre_y, centre_z)

    def draw(self):
        if not self.loaded:
            self.load_data()
        self.bounding_box = self.calc_bounding_box()
        rl.DrawModelEx(self.model, self.pos, self.rotation_axis, self.rotation_angle, self.size, self.color)
        if self.wires:
            rl.DrawBoundingBox(self.bounding_box, self.wire_color)
            rl.DrawSphere(self.calc_centre(), self.collision_radius, RED)

    def check_collision(self, other):
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(self.calc_centre(), self.collision_radius, other.pos, other.radius)
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxSphere(other.calc_bounding_box(), self.calc_centre(), self.collision_radius)
        elif isinstance(other, Actor):
            return rl.CheckCollisionSpheres(self.pos, self.collision_radius, other.pos, other.collision_radius)


class Cube(Actor):
    def __init__(self, position=(0, 0, 0), size=(10, 10, 10), color=WHITE, wires=False,
                 wire_color=DARKGRAY,
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0):
        super().__init__(model_file="", position=position, rotation_axis=rotation_axis, rotation_angle=rotation_angle,
                         size=size, color=color, wires=wires, wire_color=wire_color)
        self.loaded = False

    def load_data(self):
        self.loaded = True
        self.model = rl.LoadModelFromMesh(rl.GenMeshCube(1, 1, 1))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat
        self.model.materials[0].shader = lightSystem.shader

    def check_collision(self, other):
        if isinstance(other, Sphere):
            return rl.CheckCollisionBoxSphere(
                self.calc_bounding_box(), other.pos, other.radius
            )
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxes(self.calc_bounding_box(), other.calc_bounding_box())
        elif isinstance(other, Actor):
            return rl.CheckCollisionBoxSphere(
                self.calc_bounding_box(), other.calc_centre(), other.collision_radius
            )


class Sphere(Actor):
    def __init__(self, position=(0,0,0), radius=10, color=RED, wires=False, wire_color=DARKGRAY):
        super().__init__(model_file="", position=position, color=color, wires=wires, wire_color=wire_color,
                         collision_radius=radius)
        self.radius = radius

    def load_data(self):
        self.loaded = True
        self.model = rl.LoadModelFromMesh(rl.GenMeshSphere(self.radius, 32, 32))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat
        self.model.materials[0].shader = lightSystem.shader


def getLightSystem():
    return lightSystem


def run():
    global lightSystem, foo
    screen_width = 800
    screen_height = 640
    title = "RichLib"

    if hasattr(mod, "WIDTH"):
        screen_width = mod.WIDTH

    if hasattr(mod, "HEIGHT"):
        screen_height = mod.HEIGHT

    if hasattr(mod, "TITLE"):
        title = mod.TITLE

    if hasattr(mod, "DATA_DIR"):
        global data_dir
        data_dir = mod.DATA_DIR

    rl.SetConfigFlags(rl.FLAG_VSYNC_HINT + rl.FLAG_MSAA_4X_HINT)

    rl.InitWindow(screen_width, screen_height, title.encode('utf-8'))

    lights0 = Light([50, 50, 50], Vector([0, 0, 0]), (150,150,150,255))
    # lights1 = Light(LIGHT_POINT, [4, 2, 4 ],  Vector([0,0,0]), RED)
    # lights2 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), GREEN)
    # lights3 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), BLUE)

    lightSystem = LightSystem([0.2, 0.2, 0.0, 1.0], lights0)  # , lights1, lights2, lights3)

    rl.SetTargetFPS(60)

    if hasattr(mod, "CAMERA"):
        rl.SetCameraMode(camera[0], mod.CAMERA)

    if hasattr(mod, "init"):
        mod.init()

    while not rl.WindowShouldClose():
        if hasattr(mod, "update"):
            mod.update()
        rl.UpdateCamera(camera)
        lightSystem.update(camera.position)
        if rl.IsKeyPressed(rl.KEY_F):
            rl.ToggleFullscreen()
        if rl.IsKeyPressed(rl.KEY_ESCAPE):
            rl.Exit()
        rl.BeginDrawing()
        if hasattr(mod, "draw2dbackground"):
            mod.draw2dbackground()
        rl.BeginMode3D(camera[0])
        pyray.draw_grid(100, 10)
        if hasattr(mod, "draw"):
            mod.draw()
        if hasattr(mod, "draw3d"):
            mod.draw3d()
            lightSystem.draw()
        rl.EndMode3D()
        if hasattr(mod, "draw2d"):
            mod.draw2d()
        rl.EndDrawing()
    rl.CloseWindow()


class Keyboard:
    def __getattr__(self, kname):
        # return is a reserved word, so alias enter to return
        if kname == 'enter':
            kname = 'return'
        kname = kname.upper()
        if not kname.startswith("KEY_"):
            kname = "KEY_" + kname

        return rl.IsKeyDown(getattr(rl, kname))


keyboard = Keyboard()
