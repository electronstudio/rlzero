from rlzero import *

WIDTH = 500
HEIGHT = 500
alien = Sprite("alien.png")
animation = Animation(["alien.png","alien_hurt.png"], 5)
alien.pos = (0, 50)


def draw():
    clear()
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    animation.update(alien)

run()