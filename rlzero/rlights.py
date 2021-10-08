from raylib import *
import pyray as screen
from .util import *
import pathlib
PATH = pathlib.Path(__file__).parent

LIGHT_DIRECTIONAL=0
LIGHT_POINT=1

class LightSystem:
    MAX_LIGHTS = 4         #// Max dynamic lights supported by shader

    def __init__(self, ambient = [ 0.2, 0.2, 0.2, 1.0 ], *ls):
        self.lights = []
        self.lightsCount = 0
        self.shader = screen.load_shader(str(PATH / "basic_lighting.vs"), str(PATH / "basic_lighting.fs"))

        self.shader.locs[SHADER_LOC_MATRIX_MODEL] = GetShaderLocation(self.shader, b"matModel");
        self.shader.locs[SHADER_LOC_VECTOR_VIEW] = GetShaderLocation(self.shader, b"viewPos");

        self.ambientLoc = GetShaderLocation(self.shader, b"ambient");
        v = ffi.new("struct Vector4 *", ambient)
        SetShaderValue(self.shader, self.ambientLoc, v, SHADER_UNIFORM_VEC4);

        for light in ls:
            self.add(light)

    def add(self, light):
        light.configure(len(self.lights), self.shader)
        self.lights.append(light)
        if len(self.lights) > self.MAX_LIGHTS:
            raise Exception("Too many lights")

    def update(self, cameraPos):
        SetShaderValue(self.shader, self.shader.locs[SHADER_LOC_VECTOR_VIEW], ffi.new("struct Vector3 *",cameraPos), SHADER_UNIFORM_VEC3)
        for light in self.lights:
            light.UpdateLightValues()

    def draw(self):
        for light in self.lights:
            if light.enabled:
                DrawSphereEx(light.pos, 0.2, 8, 8, light.color)


class Light:
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = Vector(value)

    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = Vector(value)

    def __init__(self,  position,  target, color=WHITE, type=LIGHT_POINT):
        self.enabled = True
        self.type = type
        self.pos = position
        self.target = target
        self.color = color



    def configure(self, id, shader):
        self.shader = shader

        self.enabledName = f"lights[{id}].enabled"
        self.typeName = f"lights[{id}].type"
        self.posName = f"lights[{id}].position"
        self.targetName = f"lights[{id}].target"
        self.colorName = f"lights[{id}].color"

        self.enabledLoc = GetShaderLocation(shader, self.enabledName.encode('utf-8'))
        self.typeLoc = GetShaderLocation(shader, self.typeName.encode('utf-8'))
        self.posLoc = GetShaderLocation(shader, self.posName.encode('utf-8'))
        self.targetLoc = GetShaderLocation(shader, self.targetName.encode('utf-8'))
        self.colorLoc = GetShaderLocation(shader, self.colorName.encode('utf-8'))

        self.UpdateLightValues()



    def UpdateLightValues(self):
        SetShaderValue(self.shader, self.enabledLoc, ffi.new("int *",self.enabled), SHADER_UNIFORM_INT)
        SetShaderValue(self.shader, self.typeLoc, ffi.new("int *",self.type), SHADER_UNIFORM_INT)

        #// Send to shader light position values
        SetShaderValue(self.shader, self.posLoc, ffi.new("struct Vector3 *",self.pos), SHADER_UNIFORM_VEC3)

        #// Send to shader light target position values
        target =[  self.target.x, self.target.y, self.target.z ]
        SetShaderValue(self.shader, self.targetLoc, ffi.new("struct Vector3 *",target), SHADER_UNIFORM_VEC3)

        #// Send to shader light color values
        color = [self.color[0]/255.0, self.color[1]/255.0,  self.color[2]/255.0, self.color[3]/255.0]
        SetShaderValue(self.shader, self.colorLoc, ffi.new("struct Vector4 *",color), SHADER_UNIFORM_VEC4)

