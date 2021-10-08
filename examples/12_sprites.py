from rlzero import *

WIDTH = 500
HEIGHT = 500

alan = Sprite('alien.png')
alan.x = 50
alan.y = 100


def draw():
    clear()
    alan.draw()


def update():
    alan.x += 0
    if alan.x > WIDTH:
        alan.x = 0

run()

