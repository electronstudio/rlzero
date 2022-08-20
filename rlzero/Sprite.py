from raylib.colors import WHITE
import pyray as pr

from .common import find_file
from .shape import Shape

class Sprite(Shape):
    """
    2d object
    """

    @property
    def scale(self):
        """
        Multiply the scale of the object by this float. 1.0 is normal scale.
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = value

    @property
    def image_file(self):
        return self._image_file

    @image_file.setter
    def image_file(self, value):
        if self.texture:
            pr.unload_texture(self.texture)
        self._image_file = value
        self.texture = self.load_texture(value)
        self.loaded = True

    @property
    def width(self):
        return self.texture.width

    @property
    def height(self):
        return self.texture.height

    def __init__(self, image_file, pos=(0, 0), collision_radius=0,
                 rotation_angle=0, scale=1.0, color=WHITE):
        """

        :param image_file:
        :param position:
        :param collision_radius:
        :param rotation_angle:
        :param scale:
        :param color:
        """
        # super().__init__(position, collision_radius, color, wires, wire_color)

        self.pos = pos
        self.color = color
        self.texture = None


        self.image_file = image_file

        self.scale = scale

        self.rotation_angle = rotation_angle
        self.collision_radius = collision_radius

    def load_data(self):
        self.loaded = True
        self.texture = self.load_texture(self.image_file)

    def load_texture(self, file_name):
        file = find_file(file_name, ['.png', '.jpg', ''], ['.', 'data/images', 'images'])
        return pr.load_texture(file)


    # FIXME should we rename to check_collide?
    # FIXME Rectangle doesnt have equivalent method cos its not a Python class, can we patch it?
    def colliderect(self, other):
        if not self.loaded:
            self.load_data()
        r1 = pr.Rectangle(self.x, self.y, self.texture.width*self.scale, self.texture.height*self.scale)
        if isinstance(other, Sprite):
            if not other.loaded:
                other.load_data()
            r2 = pr.Rectangle(other.x, other.y, other.texture.width*other.scale, other.texture.height*other.scale)
        else:  # assume other is: <class '_cffi_backend.__CDataOwn'> cdata 'struct Rectangle'
            r2 = other
        return pr.check_collision_recs(r1, r2)

    def collidepoint(self, point):
        r1 = pr.Rectangle(self.x, self.y, self.texture.width*self.scale, self.texture.height*self.scale)
        return pr.check_collision_point_rec(point, r1)

    def draw(self):
        if not self.loaded:
            self.load_data()
        cx, cy = self.width/2, self.height/2
        px, py = rotate((cx, cy),(0,0),-self.rotation_angle)
        #print(px, py)
        x = self.x - px + cx
        y = self.y - py + cy
        pr.draw_texture_ex(self.texture, (x, y), self.rotation_angle, self.scale, self.color)

_DEG2RAD=0.01745329251

import math

def rotate(point, origin, degrees):
    radians = degrees * _DEG2RAD
    x,y = point
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = math.cos(radians)
    sin_rad = math.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y
    return qx, qy