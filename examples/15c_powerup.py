from rlzero import *
import random

WIDTH = 500
HEIGHT = 500

alan = Sprite("alien.png")
alan.pos = (400, 50)
box = Rectangle(20, 20, 100, 100)
score = 0

def draw():
    draw_rectangle_rec(box, GREEN)
    alan.draw()

def update():
    global score
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2
    if alan.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)

run()
