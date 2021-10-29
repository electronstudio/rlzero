from raylib import ffi, rl


def _fix_key(kname):
    # return is a reserved word, so alias enter to return
    #if kname == 'enter':
    #    kname = 'return'
    kname = kname.upper()
    if not kname.startswith("KEY_"):
        kname = "KEY_" + kname
    return kname


class Keyboard:
    """
    Handles input from keyboard
    """
    def __getattr__(self, kname):
        f = _fix_key(kname)
        return rl.IsKeyDown(getattr(rl, f))



    def key_down(self, kname):
        """
        Test if key is currently down
        """
        f = _fix_key(kname)
        return rl.IsKeyDown(getattr(rl, f))

    def key_pressed(self, kname):
        """
        Test if key was pressed recently
        """
        f = _fix_key(kname)
        return rl.IsKeyPressed(getattr(rl, f))


class Keys:
    def __getattr__(self, kname):
        k = getattr(rl, _fix_key(kname))
        print(k)
        return k
