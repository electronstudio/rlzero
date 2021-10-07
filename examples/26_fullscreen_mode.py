from rlzero import *

WIDTH = 500
HEIGHT = 500

alien = Sprite("alien")

def draw():
    clear()
    alien.draw()

def update():
    if keyboard.f1:
        toggle_fullscreen()
    if keyboard.enter:
        exit()

run()