import random
from rlzero import *

WIDTH = 600
HEIGHT = 600

background = Sprite("background")
player = Sprite("player")
player.x = 200
player.y = 200

enemy = Sprite("alien")
player2 = Sprite("player")
coin = Sprite("coin", pos=(300,300))
score = 0
time = 20


def draw2d():
    clear()
    background.draw()
    player.draw()
    enemy.draw()
    player2.draw()
    coin.draw()
    draw_text("My game", 200, 0, 20, RED)
    score_string = str(score)
    draw_text(score_string, 0,0, 20, GREEN)
    time_string = str(round(time))
    draw_text(time_string, 50,0, 20, GREEN)

def update(delta):
    global score, time
    time = time - delta
    if time <= 0:
        print("time out")
        exit()
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y < 0:
        player.y = HEIGHT
    if player.y > HEIGHT:
        player.y = 0

    if enemy.x < player.x:
        enemy.x = enemy.x + 1
    if enemy.x > player.x:
        enemy.x = enemy.x - 1
    if enemy.y < player.y:
        enemy.y = enemy.y + 1
    if enemy.y > player.y:
        enemy.y = enemy.y - 1
    if player.colliderect(enemy):
        print("player 1 hit enemy")
        exit()

    if keyboard.d:
        player2.x = player2.x + 4
    if keyboard.a:
        player2.x = player2.x - 4
    if keyboard.s:
        player2.y = player2.y + 4
    if keyboard.w:
        player2.y = player2.y - 4
    if player.colliderect(player2):
        print("player1 hit player 2")
        exit()

    if coin.colliderect(player):
        coin.x = random.randint(0, WIDTH)
        coin.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)


run()