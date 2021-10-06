from rlzero import *

alien = Sprite('alien')
alien.pos = (0, 50)

def draw():
    clear()
    alien.draw()

def update():
    if keyboard.right or gamepad.right:
        alien.x = alien.x + 2
    elif keyboard.left or gamepad.left:
        alien.x = alien.x - 2

run()

