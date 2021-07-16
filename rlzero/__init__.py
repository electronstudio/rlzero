""" Richlib Zero, simple access to Raylib
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
camera.projection = rl.CAMERA_PERSPECTIVE

mod = sys.modules['__main__']


def clear(color=RAYWHITE):
    """
    Clear the screen
    :param Color color:
    """
    rl.ClearBackground(Color(color))


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
        self._color = Color(value)

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


class Sound:
    """
    A sound effect loaded from a wav file.
    """
    def __init__(self, file, volume=1.0, pitch=1.0):
        self.sound = None
        self.file = file
        self.loaded = False
        self.volume = volume
        self.pitch = pitch

    def load_data(self):
        """
        Loads the sound data from wav file on disk.
        Will be called automatically the first time the sound is played.
        """
        self.loaded = True
        file = data_dir + self.file + '.wav'
        if not os.path.isfile(file):
            file = str(PATH / 'sounds' / self.file) + '.wav'
        if not os.path.isfile(file):
            raise Exception(f"file {self.file} does not exist")
        self.sound = rl.LoadSound(file.encode('utf-8'))
        rl.SetSoundVolume(self.sound, self._volume)
        rl.SetSoundPitch(self.sound, self._pitch)

    def play(self):
        """
        Play the sound using the current volume and pitch.
        """
        if not self.loaded:
            self.load_data()
        rl.PlaySound(self.sound)

    @property
    def volume(self):
        """
        How loud to play the sound. 0.0 is silent, 1.0 is full.
        """
        return self._volume

    @volume.setter
    def volume(self, value):
        if (self.loaded):
            rl.SetSoundVolume(self.sound, value)
        self._volume = value

    @property
    def pitch(self):
        """
        Multiply the same frequency by this float. 1.0 is default pitch.
        """
        return self._pitch

    @pitch.setter
    def pitch(self, value):
        if (self.loaded):
            rl.SetSoundPitch(self.sound, value)
        self._pitch = value


class Actor(Shape):
    """
    3d object
    """

    @property
    def size(self):
        """
        Multiply the size of the object by this float. 1.0 is normal size.
        """
        return self._size

    @size.setter
    def size(self, value):
        self._size = Vector(value)

    def __init__(self, model_file, position=(0, 0, 0), collision_radius=0, texture_file="",
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0, size=(1, 1, 1), color=WHITE, wires=False,
                 wire_color=DARKGRAY):
        """

        :param model_file:
        :param position:
        :param collision_radius:
        :param texture_file:
        :param rotation_axis:
        :param rotation_angle:
        :param size:
        :param color:
        :param wires:
        :param wire_color:
        """
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
        """
        Loads the 3d model data from obj file on disk.
        Will be called automatically the first time the model is drawn.
        """
        self.loaded = True
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
            self.model.materials[0].maps[rl.MATERIAL_MAP_DIFFUSE].texture = texture

        self.model.materials[0].shader = lightSystem.shader
        self.bounding_box = self.calc_bounding_box()

    def calc_bounding_box(self):
        """
        Calculates a box big enough to contain the object.
        :return: The bounding box.
        """
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
        """
        Calculates the centre of the object.

        :returns: Vector -- centre position in global space
        """
        centre_x = (self.bounding_box.max.x + self.bounding_box.min.x) / 2
        centre_y = (self.bounding_box.max.y + self.bounding_box.min.y) / 2
        centre_z = (self.bounding_box.max.z + self.bounding_box.min.z) / 2
        return (centre_x, centre_y, centre_z)

    def draw(self):
        """
        Draws the object.
        Should be called from draw() or draw3d()
        """

        if not self.loaded:
            self.load_data()
        self.bounding_box = self.calc_bounding_box()
        rl.DrawModelEx(self.model, self.pos, self.rotation_axis, self.rotation_angle, self.size, self.color)
        if self.wires:
            rl.DrawBoundingBox(self.bounding_box, self.wire_color)
            rl.DrawSphere(self.calc_centre(), self.collision_radius, RED)

    def check_collision(self, other):
        """
        Check if the object is currently colliding with another object

        :param other: Actor - The other object
        :return: bool
        """
        if not self.loaded:
            self.load_data()
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(self.calc_centre(), self.collision_radius, other.pos, other.radius)
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxSphere(other.calc_bounding_box(), self.calc_centre(), self.collision_radius)
        elif isinstance(other, Actor):
            return rl.CheckCollisionSpheres(self.calc_centre(), self.collision_radius, other.calc_centre(),
                                            other.collision_radius)


class Cube(Actor):
    """
    Actor with cube shaped mesh generated rather than loaded from file.
    """

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
        if not self.loaded:
            self.load_data()
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
    """
    Actor with sphere shaped mesh generated rather than loaded from file.
    """

    def __init__(self, position=(0, 0, 0), radius=10, color=RED, wires=False, wire_color=DARKGRAY):
        super().__init__(model_file="", position=position, color=color, wires=wires, wire_color=wire_color,
                         collision_radius=radius)
        self.radius = radius

    def load_data(self):
        self.loaded = True
        self.model = rl.LoadModelFromMesh(rl.GenMeshSphere(self.radius, 32, 32))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat
        self.model.materials[0].shader = lightSystem.shader

    def check_collision(self, other):
        if not self.loaded:
            self.load_data()
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(self.pos, self.radius, other.pos, other.radius)
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxSphere(other.calc_bounding_box(), self.pos, self.radius)
        elif isinstance(other, Actor):
            return rl.CheckCollisionSpheres(self.pos, self.radius, other.calc_centre(), other.collision_radius)


def getLightSystem():
    return lightSystem

def _pre_setup():
    global lightSystem
    rl.SetConfigFlags(rl.FLAG_VSYNC_HINT + rl.FLAG_MSAA_4X_HINT)

    rl.InitWindow(1, 1, "title".encode('utf-8'))
    rl.InitAudioDevice()

    lights0 = Light([50, 50, 50], Vector([0, 0, 0]), (150, 150, 150, 255))
    # lights1 = Light(LIGHT_POINT, [4, 2, 4 ],  Vector([0,0,0]), RED)
    # lights2 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), GREEN)
    # lights3 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), BLUE)

    lightSystem = LightSystem([0.2, 0.2, 0.0, 1.0], lights0)  # , lights1, lights2, lights3)

    rl.SetTargetFPS(60)

def _setup():

    screen_width = 800
    screen_height = 640
    title = "RichLib"



    if hasattr(mod, "WIDTH"):
        screen_width = mod.WIDTH

    if hasattr(mod, "HEIGHT"):
        screen_height = mod.HEIGHT

    if hasattr(mod, "TITLE"):
        title = mod.TITLE

    pyray.set_window_size(screen_width, screen_height, title)

    if hasattr(mod, "DATA_DIR"):
        global data_dir
        data_dir = mod.DATA_DIR

    if hasattr(mod, "CAMERA"):
        rl.SetCameraMode(camera[0], mod.CAMERA)

    if hasattr(mod, "init"):
        mod.init()

def _main_loop():
    if hasattr(mod, "update"):
        if (mod.update.__code__.co_argcount > 0):
            mod.update(rl.GetFrameTime())
        else:
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

def run():
    _setup()

    while not rl.WindowShouldClose():
        _main_loop()

    rl.CloseWindow()


def fix_key(kname):
    # return is a reserved word, so alias enter to return
    if kname == 'enter':
        kname = 'return'
    kname = kname.upper()
    if not kname.startswith("KEY_"):
        kname = "KEY_" + kname
    return kname


class Keyboard:
    def __getattr__(self, kname):
        f = fix_key(kname)
        return rl.IsKeyDown(getattr(rl, f))

    def key_down(self, kname):
        f = fix_key(kname)
        return rl.IsKeyDown(getattr(rl, f))

    def key_pressed(self, kname):
        f = fix_key(kname)
        return rl.IsKeyPressed(getattr(rl, f))


class Mouse:
    def get_position_on_ground(self, ground_level):
        pos = pyray.get_mouse_position()
        ray = pyray.get_mouse_ray(pos, camera[0])
        rayhit = screen.get_collision_ray_ground(ray, ground_level)
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
        ray = pyray.get_mouse_ray(pos, camera[0])
        return pyray.check_collision_ray_box(ray, actor.calc_bounding_box())


class Gamepad:
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



mouse = Mouse()
"""Default Mouse object"""

keyboard = Keyboard()
"""Default Keyboard object"""

gamepad = Gamepad(0)
"""First Gamepad object"""

gamepad0 = gamepad

gamepad1 = Gamepad(1)
"""Second Gamepad object"""


_pre_setup()
