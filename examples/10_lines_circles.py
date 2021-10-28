from rlzero import *

WIDTH = 500
HEIGHT = 500

def draw():
    draw_circle_lines(250, 250, 50, WHITE)
    draw_circle(250, 100, 50, RED)
    draw_line(150, 20, 150, 450, PURPLE)
    draw_line(150, 20, 350, 20, PURPLE)

run()