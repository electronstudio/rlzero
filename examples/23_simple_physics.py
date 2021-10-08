from rlzero import *

WIDTH = 500
HEIGHT = 500

ball = Rectangle(200, 400, 20, 20)
vx = 1
vy = 1

def draw():
    clear()
    draw_rectangle_rec(ball, RED)

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.x > WIDTH or ball.x < 0:
        vx = -vx
    if ball.y > HEIGHT or ball.y < 0:
        vy = -vy

run()