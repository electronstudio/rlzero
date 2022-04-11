from rlzero import *

WIDTH = 500
HEIGHT = 500

alan = Sprite('alien.png')
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
    if keyboard.up:
        alan.rotation_angle = alan.rotation_angle + 1
    elif keyboard.down:
        alan.rotation_angle = alan.rotation_angle - 1
    #box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
    if alan.colliderect(box):
        print("hit")


run()

