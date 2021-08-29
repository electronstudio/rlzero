"""
    Demo game
"""

from rlzero import *
import random
import time

TIME = 20
NUMBER_OF_BALLS = 10
JUMP_POWER = 2

start_time = time.time()
time_left = TIME

CAMERA =pyray.CAMERA_PERSPECTIVE

balls = []
for i in range(0, NUMBER_OF_BALLS):
    ball = Sphere()
    ball.x = random.randint(-300, 300)
    ball.y = random.randint(10, 40)
    ball.z = random.randint(-300, 0)
    ball.color = 'green'
    balls.append(ball)

score = 0

DATA_DIR="data"

wiz = Actor('rpg_characters/Wizard')
wiz.size = (10, 10, 10)
wiz.collision_radius = 5

wiz.yv = 0
wiz.xv = 0
wiz.zv = 0

sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5


def draw():
    clear()
    wiz.draw()
    for ball in balls:
        ball.draw()
        pyray.draw_circle_3d((ball.pos.x, 0, ball.pos.z),10,(1,0,0),90,BLACK)


def draw2d():
    if (time_left > 0):
        screen.draw_text(f"Score: {score}       Time: {time_left}", 0, 0, 50, VIOLET)
    else:
        screen.draw_text(f"Your Score: {score}\nOUT OF TIME", 30, 50, 50, RED)


def update(delta):
    global score
    global time_left

    print("frame delta: ", delta)
    camera.target = wiz.pos

    time_left = int(TIME + (start_time - time.time()))
    if time_left <= 0:
        return

    wiz.yv -= 0.05

    wiz.x += wiz.xv
    wiz.y += wiz.yv
    wiz.z += wiz.zv

    if wiz.y <= 0:  # Only control when wiz is on ground
        if keyboard.right:
            wiz.xv += 0.1
        elif keyboard.left:
            wiz.xv -= 0.1
        if keyboard.down:
            wiz.zv += 0.1
        elif keyboard.up:
            wiz.zv -= 0.1

        if keyboard.space:
            wiz.yv = JUMP_POWER

        if wiz.xv > 0.05:
            wiz.xv -= 0.05
        elif wiz.xv < -0.05:
            wiz.xv += 0.05

        if wiz.zv > 0.05:
            wiz.zv -= 0.05
        elif wiz.zv < -0.05:
            wiz.zv += 0.05

        wiz.y = 0

    for ball in balls:
        if wiz.check_collision(ball):
            balls.remove(ball)
            sound.play()
            score += 1


run()

""" TODO
    gamepad controls
    change jump power, number of balls
    second player
    enemy that chases player

"""
