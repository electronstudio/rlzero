from rlzero import *

WIDTH = 500
HEIGHT = 500

ball = Rectangle(150, 400, 20, 20)
bat = Rectangle(200, 480, 60, 20)
vx = 4
vy = 4

def draw():
    draw_rectangle_rec(ball, RED)
    draw_rectangle_rec(bat, WHITE)

def update():
    global vx, vy
    ball.x += vx
    ball.y += vy
    if ball.x > WIDTH or ball.x < 0:
        vx = -vx
    if check_collision_recs(bat, ball) or ball.y < 0:
        vy = -vy
    if ball.y > HEIGHT:
        exit()
    if(keyboard.right):
        bat.x += 2
    elif(keyboard.left):
        bat.x -= 2

run()

