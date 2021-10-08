from .common import find_file
import pyray as pr

def Texture(file):
    texture = pr.load_texture(find_file(file, ['.png', '.jpg', ''], ['.', 'data/images', 'images']))
    return texture

class Vector(list):
    @property
    def x(self):
        return self[0]

    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]

    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]

    @z.setter
    def z(self, value):
        self[2] = value

    @property
    def w(self):
        return self[3]

    @w.setter
    def w(self, value):
        self[3] = value

class Color(list):
    def __init__(self, s):
        if isinstance(s, str):
            super().__init__(globals()[s.upper()])
        else:
            super().__init__(s)
        if len(self) == 3:
            self.append(255)

    @property
    def r(self):
        return self[0]

    @r.setter
    def r(self, value):
        self[0] = value

    @property
    def g(self):
        return self[1]

    @g.setter
    def g(self, value):
        self[1] = value

    @property
    def b(self):
        return self[2]

    @b.setter
    def b(self, value):
        self[2] = value

    @property
    def a(self):
        return self[3]

    @a.setter
    def a(self, value):
        self[3] = value

