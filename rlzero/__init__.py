""" RL Zero, simple access to Raylib
"""
__version__ = '0.1'

from raylib.static import ffi, rl
# from ..dynamic import ffi, raylib as rl
from raylib.colors import *
from .util import *

import sys
import os
import rlzero.rlights as Lights
import rlzero.globals as Globals
from .shape import *
from .sound import *
#import rlzero.keyboard as Keyboard
from .keyboard import Keyboard
from .mouse import Mouse
from .gamepad import Gamepad
from raylib.pyray import PyRay

pyray = PyRay()
screen = pyray

camera = ffi.new("struct Camera3D *")
camera.position = (0.0, 100, 100)
camera.target = (0.0, 0.0, 0.0)
camera.up = (0, 1, 0)
camera.fovy = 45
camera.projection = rl.CAMERA_PERSPECTIVE

Globals.camera = camera

# mod = sys.modules['__main__']


def clear(color=RAYWHITE):
    """
    Clear the screen
    :param Color color:
    """
    rl.ClearBackground(Color(color))



def getLightSystem():
    return globals.light_system


def _pre_setup():
    #global lightSystem
    rl.SetConfigFlags(rl.FLAG_VSYNC_HINT + rl.FLAG_MSAA_4X_HINT)

    rl.InitWindow(1, 1, "title".encode('utf-8'))
    rl.InitAudioDevice()

    lights0 = Lights.Light([50, 50, 50], Vector([0, 0, 0]), (150, 150, 150, 255))
    # lights1 = Light(LIGHT_POINT, [4, 2, 4 ],  Vector([0,0,0]), RED)
    # lights2 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), GREEN)
    # lights3 = Light(LIGHT_POINT, [ 0, 4, 2 ],  Vector([0,0,0]), BLUE)

    globals.light_system = Lights.LightSystem([0.2, 0.2, 0.0, 1.0], lights0)  # , lights1, lights2, lights3)

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
        #global data_dir
        Globals.data_dir = mod.DATA_DIR

    if hasattr(mod, "CAMERA"):
        rl.SetCameraMode(camera[0], mod.CAMERA)

    if hasattr(mod, "init"):
        mod.init()


def _main_loop():
    #print(mod)
    if hasattr(mod, "update"):
        if (mod.update.__code__.co_argcount > 0):
            mod.update(rl.GetFrameTime())
        else:
            mod.update()
    rl.UpdateCamera(camera)
    Globals.light_system.update(camera.position)
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
        Globals.light_system.draw()
    rl.EndMode3D()
    if hasattr(mod, "draw2d"):
        mod.draw2d()
    rl.EndDrawing()


def run(m=sys.modules['__main__']):
    global mod
    mod = m
    _setup()
    while not rl.WindowShouldClose():
        _main_loop()

    rl.CloseWindow()





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
