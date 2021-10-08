from rlzero import *


WIDTH = 500
HEIGHT = 500

class MySprite(Sprite):
    vx = 1
    vy = 1

ball = MySprite('alien.png')

def draw():
    clear()
    ball.draw()

def update():
    ball.x += ball.vx
    ball.y += ball.vy
    if ball.x > WIDTH or ball.x < 0:
        ball.vx = -ball.vx
    if ball.y > HEIGHT or ball.y < 0:
        ball.vy = -ball.vy


run()