import pyray as pr
from .common import find_file


class Animation:
    def __init__(self, files, fps=25):
        self.files = files
        self.textures = [None] * len(files)
        self.frame = 0
        self.interval = 1.0/float(fps)
        self.time = 0.0

    def get_texture(self, i):
        i = i % len(self.textures)-1
        if self.textures[i]:
            return self.textures[i]
        else:
            file = find_file(self.files[i], ['.png', '.jpg', ''], ['.', 'data/images', 'images'])
            self.textures[i] = pr.load_texture(file)
            return self.textures[i]

    def update(self, sprite):
        self.time += pr.get_frame_time()
        if self.time >= self.interval:
            self.frame += 1
            self.time -= self.interval

        sprite.texture = self.get_texture(self.frame)


