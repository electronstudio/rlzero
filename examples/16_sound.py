from rlzero import *

my_sound = Sound("eep.wav")

def draw():
    clear_background(WHITE)

def update():
    if keyboard.space:
        my_sound.play()

run()