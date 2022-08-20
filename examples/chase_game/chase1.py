from rlzero import *

WIDTH = 600
HEIGHT = 600

background = Sprite("background")
player = Sprite("player")
player.x = 200
player.y = 200

def draw():
    clear()
    background.draw()
    player.draw()

def update():
    if keyboard.right:
        player.x = player.x + 4
    if keyboard.left:
        player.x = player.x - 4
    if keyboard.down:
        player.y = player.y + 4
    if keyboard.up:
        player.y = player.y - 4

run()
