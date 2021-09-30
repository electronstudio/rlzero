from rlzero import *

WIDTH = 500
HEIGHT = 500

box = screen.Rectangle(20, 20, 50, 50)

def draw():
    clear()
    screen.draw_rectangle_rec(box, RED)

def update():
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0

run()