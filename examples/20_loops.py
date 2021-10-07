from rlzero import *

WIDTH = 500
HEIGHT = 500

def draw():
    clear()
    for x in range(0, WIDTH, 40):
        draw_circle(x, 20, 20, RED)

    for x in range(0, WIDTH, 40):
        for y in range(60, HEIGHT, 40):
            draw_circle(x, y, 10, GREEN)

run()