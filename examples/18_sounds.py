"""
    The 'eep' sound is built-in.  Other sounds must be provided as wav files.
    Click the mouse to play the sound.
"""
from richlib import *

sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5

def draw():
    clear()


def update():
    if mouse.clicked:
        sound.play()

run()

"""TODO
    Change the pitch each time the mouse is clicked.
    Edit program 17 so that it plays a sound when you hit the cube.
"""
