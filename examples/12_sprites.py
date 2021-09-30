from rlzero import *

WIDTH = 500
HEIGHT = 500

alien = Sprite('alien.png')
alien.x = 0
alien.y = 50


def draw():
    clear()
    alien.draw()


def update():
    alien.x += 2
    if alien.x > WIDTH:
        alien.x = 0

run()

