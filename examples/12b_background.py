from rlzero import *

WIDTH = 500
HEIGHT = 500

alan = Sprite('alien.png')
alan.x = 0
alan.y = 50

background = Sprite('background.png')

def draw():
    clear()
    background.draw()
    alan.draw()


def update():
    alan.x += 2
    if alan.x > WIDTH:
        alan.x = 0

run()

