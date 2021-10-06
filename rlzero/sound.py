from raylib import ffi, rl
import rlzero.globals as Globals
import os


class Sound:
    """
    A sound effect loaded from a wav file.sssss
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
        file = Globals.data_dir + os.path.sep + 'sounds' + os.path.sep + self.file + '.wav'
        if not os.path.isfile(file):
            file = str(Globals.PATH / 'sounds' / self.file) + '.wav'
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

