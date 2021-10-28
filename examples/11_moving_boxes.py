from rlzero import *

WIDTH = 500
HEIGHT = 500

box = Rectangle(20, 20, 50, 50)


def draw():
    draw_rectangle_rec(box, RED)

def update():
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0

run()