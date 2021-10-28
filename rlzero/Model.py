import raylib as rl
from raylib.colors import *
from .common import _gen_file_paths, find_file
from .util import *
import rlzero.globals as Globals
import os



from raylib.colors import WHITE


from .common import find_file
from .shape import Shape


class Model(Shape):
    """
    3d object
    """

    @property
    def scale(self):
        """
        Multiply the scale of the object by this float. 1.0 is normal scale.
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        self._scale = Vector(value)

    def __init__(self, model_file, pos=(0, 0, 0), collision_radius=0, texture_file="",
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0, scale=(1, 1, 1), color=WHITE,
                 wires=False,
                 wire_color=DARKGRAY):
        """

        :param model_file:
        :param position:
        :param collision_radius:
        :param texture_file:
        :param rotation_axis:
        :param rotation_angle:
        :param scale:
        :param color:
        :param wires:
        :param wire_color:
        """
        # super().__init__(position, collision_radius, color, wires, wire_color)

        self.pos = pos
        self.color = color
        self.wire_color = wire_color
        self.wires = wires

        self.model_file = model_file
        if texture_file == "":
            texture_file = model_file + "_diffuse"
        self.texture_file = texture_file
        self.scale = scale
        self.rotation_axis = rotation_axis
        self.rotation_angle = rotation_angle
        self.collision_radius = collision_radius
        self.loaded = False

    def load_data(self):
        """
        Loads the 3d model data from glb file on disk.
        Will be called automatically the first time the model is drawn.
        """
        self.loaded = True
        file = Globals.data_dir + os.path.sep + 'models' + os.path.sep + self.model_file + '.glb'
        print("trying ",file)
        if not os.path.isfile(file):
            file = str(Globals.PATH / 'models' / self.model_file) + '.glb'
            print("trying ",file)
        if not os.path.isfile(file):
            raise Exception(f"file {self.model_file} does not exist")

        self.model = rl.LoadModel(file.encode('utf-8'))


        self.model.materials[0].shader = Globals.light_system.shader
        self.bounding_box = self.calc_bounding_box()

    def load_data_obj(self):
        """
        Loads the 3d model data from obj file on disk.
        """
        self.loaded = True
        file = Globals.data_dir + self.model_file + '.obj'
        if not os.path.isfile(file):
            file = str(Globals.PATH / 'models' / self.model_file) + '.obj'
        if not os.path.isfile(file):
            raise Exception(f"file {self.model_file} does not exist")

        self.model = rl.LoadModel(file.encode('utf-8'))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat

        tfile = Globals.data_dir + self.texture_file + '.png'
        if not os.path.isfile(tfile):
            tfile = str(Globals.PATH / 'models' / self.texture_file) + '.png'

        texture = rl.LoadTexture(tfile.encode('utf-8'))
        if texture.format:
            self.model.materials[0].maps[rl.MATERIAL_MAP_DIFFUSE].texture = texture

        self.model.materials[0].shader = Globals.light_system.shader
        self.bounding_box = self.calc_bounding_box()


    def calc_bounding_box(self):
        """
        Calculates a box big enough to contain the object.
        :return: The bounding box.
        """
        if not hasattr(self, 'model'):
            return ((0, 0, 0), (0, 0, 0))
        bb = rl.MeshBoundingBox(self.model.meshes[0])

        bb.min.x *= self.scale.x
        bb.min.y *= self.scale.y
        bb.min.z *= self.scale.z
        bb.max.x *= self.scale.x
        bb.max.y *= self.scale.y
        bb.max.z *= self.scale.z

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
        rl.DrawModelEx(self.model, self.pos, self.rotation_axis, self.rotation_angle, self.scale,
                       self.color)
        if self.wires:
            rl.DrawBoundingBox(self.bounding_box, self.wire_color)
            rl.DrawSphere(self.calc_centre(), self.collision_radius, RED)

    def check_collision(self, other):
        """
        Check if the object is currently colliding with another object

        :param other: Model - The other object
        :return: bool
        """
        if not self.loaded:
            self.load_data()
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(self.calc_centre(), self.collision_radius, other.pos,
                                            other.radius)
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxSphere(other.calc_bounding_box(), self.calc_centre(),
                                              self.collision_radius)
        elif isinstance(other, Model):
            return rl.CheckCollisionSpheres(self.calc_centre(), self.collision_radius,
                                            other.calc_centre(),
                                            other.collision_radius)




class Cube(Model):
    """
    Model with cube shaped mesh generated rather than loaded from file.
    """

    def __init__(self, pos=(0, 0, 0), scale=(10, 10, 10), color=WHITE, wires=False,
                 wire_color=DARKGRAY,
                 rotation_axis=Vector([0, 1, 0]), rotation_angle=0):
        super().__init__(model_file="", pos=pos, rotation_axis=rotation_axis,
                         rotation_angle=rotation_angle,
                         scale=scale, color=color, wires=wires, wire_color=wire_color)
        self.loaded = False

    def load_data(self):
        self.loaded = True
        self.model = rl.LoadModelFromMesh(rl.GenMeshCube(1, 1, 1))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat
        self.model.materials[0].shader = Globals.light_system.shader

    def check_collision(self, other):
        if not self.loaded:
            self.load_data()
        if isinstance(other, Sphere):
            return rl.CheckCollisionBoxSphere(
                self.calc_bounding_box(), other.pos, other.radius
            )
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxes(self.calc_bounding_box(), other.calc_bounding_box())
        elif isinstance(other, Model):
            return rl.CheckCollisionBoxSphere(
                self.calc_bounding_box(), other.calc_centre(), other.collision_radius
            )


class Sphere(Model):
    """
    Model with sphere shaped mesh generated rather than loaded from file.
    """

    def __init__(self, position=(0, 0, 0), radius=10, color=RED, wires=False, wire_color=DARKGRAY):
        super().__init__(model_file="", position=position, color=color, wires=wires,
                         wire_color=wire_color,
                         collision_radius=radius)
        self.radius = radius

    def load_data(self):
        self.loaded = True
        self.model = rl.LoadModelFromMesh(rl.GenMeshSphere(self.radius, 32, 32))
        mat = rl.LoadMaterialDefault()
        self.model.materials[0] = mat
        self.model.materials[0].shader = Globals.light_system.shader

    def check_collision(self, other):
        if not self.loaded:
            self.load_data()
        if isinstance(other, Sphere):
            return rl.CheckCollisionSpheres(self.pos, self.radius, other.pos, other.radius)
        elif isinstance(other, Cube):
            return rl.CheckCollisionBoxSphere(other.calc_bounding_box(), self.pos, self.radius)
        elif isinstance(other, Model):
            return rl.CheckCollisionSpheres(self.pos, self.radius, other.calc_centre(),
                                            other.collision_radius)



