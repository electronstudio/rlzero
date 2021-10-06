from rlzero import *

WIDTH = 500
HEIGHT = 500

alien = Sprite('alien')
alien.pos = (400, 50)
box = screen.Rectangle(20, 20, 100, 100)

def draw():
    clear()
    screen.draw_rectangle_rec(box, RED)
    alien.draw()

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
    if alien.colliderect(box):
        print("hit")


run()

