from rlzero import *

WIDTH = 500
HEIGHT = 500

alan = Sprite("alien.png")
alan.pos = (400, 50)
box = Rectangle(20, 20, 100, 100)

def draw():
    draw_rectangle_rec(box, RED)
    alan.draw()

def update():
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2
    if box.x < alan.x:
        box.x = box.x + 1
    if box.x > alan.x:
        box.x = box.x - 1
    if alan.colliderect(box):
        exit()

run()