from rlzero import *

# wiggle your mouse around the screen!

alien = Sprite("alien")

def draw():
    clear()
    alien.draw()

def on_mouse_move(pos):
    alien.pos = pos

run()