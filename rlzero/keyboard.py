from .util import *
from raylib.pyray import PyRay
from raylib.static import ffi, rl
pyray = PyRay()

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

