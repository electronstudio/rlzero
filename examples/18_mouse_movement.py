from rlzero import *

# wiggle your mouse around the screen!

alan = Sprite("alien.png")

def draw():
    alan.draw()

def on_mouse_move(pos):
    alan.pos = pos

run()