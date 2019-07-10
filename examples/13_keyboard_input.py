from richlib import *

alien = Actor('trooper')
alien.size = (20,20,20)
alien.pos = (0, 10, 10)

def draw():
    clear()
    alien.draw()


def update():
    if keyboard.right:
        alien.x = alien.x + 1
    elif keyboard.left:
        alien.x = alien.x - 1

run()


"""TODO
    make the alien move up and down as well as left and right
    use the += operator to change the alien.x
    use the 'or' operator to allow WASD keys to move the alien
    in addition to the cursor keys
    make alien wrap around when he moves off edge of screen
"""
