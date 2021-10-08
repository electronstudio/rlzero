""" RL Zero, simple access to Raylib
"""

from raylib import *
from raylib.colors import *
from .util import *

import builtins
import sys
import os
import rlzero.rlights as Lights
import rlzero.globals as Globals
from .Sprite import Sprite
from .shape import *
from .Sound import *
from .Model import *
from .Keyboard import Keyboard
from .Mouse import Mouse
from .Gamepad import Gamepad
from .Animation import Animation


import pyray as pr


camera = ffi.new("struct Camera3D *")
camera.position = (0.0, 100, 100)
camera.target = (0.0, 0.0, 0.0)
camera.up = (0, 1, 0)
camera.fovy = 45
camera.projection = rl.CAMERA_PERSPECTIVE

Globals.camera = camera

# mod = sys.modules['__main__']
current_module = __import__(__name__)
#setattr(current_module, 'draw_pixel', pyray.draw_pixel)
#draw_pixel = pyray.draw_pixel

method_list = [func for func in dir(pr) if callable(getattr(pr, func))
               and not func.startswith("__")  # and not func[0].isupper()
               ]
for m in method_list:
    #print(str(m))
    #setattr(builtins, m, getattr(pyray, m))
    if not hasattr(current_module, m):
        setattr(current_module, m, getattr(pr, m))


def clear(color=BLACK):
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

    pr.set_window_size(screen_width, screen_height, title)

    if hasattr(mod, "DATA_DIR"):
        #global data_dir
        Globals.data_dir = mod.DATA_DIR
        print("SET dAtaDIR ",mod.DATA_DIR)

    if hasattr(mod, "CAMERA"):
        rl.SetCameraMode(camera[0], mod.CAMERA)

    if hasattr(mod, "init"):
        mod.init()

old_mouse_pos=(0,0)

def _call_backs():
    pos = (pr.get_mouse_x(), pr.get_mouse_y())
    if hasattr(mod, "on_mouse_move"):
        global old_mouse_pos
        if not pos == old_mouse_pos:
            old_mouse_pos = pos
            mod.on_mouse_move(pos)

    if hasattr(mod, "on_mouse_down"):
        for i in range(10):
            if pr.is_mouse_button_down(i):
                mod.on_mouse_down(pos, i)

    if hasattr(mod, "on_mouse_up"):
        for i in range(10):
            if pr.is_mouse_button_up(i):
                mod.on_mouse_up(pos, i)

    if hasattr(mod, "on_mouse_pressed"):
        for i in range(10):
            if pr.is_mouse_button_pressed(i):
                mod.on_mouse_pressed(pos, i)

    if hasattr(mod, "on_mouse_released"):
        for i in range(10):
            if pr.is_mouse_button_released(i):
                mod.on_mouse_released(pos, i)

    if hasattr(mod, "on_key_pressed"):
        key = get_key_pressed()
        if key != 0:
            mod.on_key_pressed(key)

def _main_loop():

    if hasattr(mod, "update"):
        if (mod.update.__code__.co_argcount > 0):
            mod.update(rl.GetFrameTime())
        else:
            mod.update()

    _call_backs()

    UpdateCamera(camera)
    Globals.light_system.update(camera.position)
    if rl.IsKeyPressed(rl.KEY_F):
        rl.ToggleFullscreen()
    if rl.IsKeyPressed(rl.KEY_ESCAPE):
        rl.Exit()
    rl.BeginDrawing()
    if hasattr(mod, "draw2dbackground"):
        mod.draw2dbackground()
    rl.BeginMode3D(camera[0])
    pr.draw_grid(100, 10)
    if hasattr(mod, "draw3d"):
        mod.draw3d()
        Globals.light_system.draw()
    rl.EndMode3D()
    if hasattr(mod, "draw2d"):
        mod.draw2d()
    if hasattr(mod, "draw"):
        mod.draw()
    rl.EndDrawing()


def run(m=sys.modules['__main__']):
    global mod
    mod = m
    _setup()
    while not WindowShouldClose():
        _main_loop()

    CloseWindow()





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

