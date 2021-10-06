from rlzero import *
import random

WIDTH = 500
HEIGHT = 500

alien = Sprite("alien")
alien.pos = (400, 50)
box = Rectangle(20, 20, 100, 100)
score = 0

def draw():
    clear()
    draw_rectangle_rec(box, GREEN)
    alien.draw()

def update():
    global score
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    if alien.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)

run()
