from rlzero import *

WIDTH = 500
HEIGHT = 500

def draw():
    clear()
    screen.draw_circle_lines(250, 250, 50, WHITE)
    screen.draw_circle(250, 100, 50, RED)
    screen.draw_line(150, 20, 150, 450, PURPLE)
    screen.draw_line(150, 20, 350, 20, PURPLE)

run()