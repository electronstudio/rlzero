from rlzero import *
DATA_DIR="data"

wiz = Model('rpg_characters/Wizard')
wiz.size = (20,20,20)
wiz.pos = (0, 10, 10)

def draw():
    clear()
    wiz.draw()

def update():
    if keyboard.right:
        wiz.x = wiz.x + 1
    elif keyboard.left:
        wiz.x = wiz.x - 1

run()

"""TODO
    make the wiz move up and down as well as left and right
    use the += operator to change the wiz.x
    use the 'or' operator to allow WASD keys to move the wiz
    in addition to the cursor keys
    make wiz wrap around when he moves off edge of screen
"""
