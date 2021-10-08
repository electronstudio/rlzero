from rlzero import *

alan = Sprite('alien.png')
alan.pos = (0, 50)

def draw():
    clear()
    alan.draw()

def update():
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2

run()