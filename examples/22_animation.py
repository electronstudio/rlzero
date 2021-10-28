from rlzero import *

WIDTH = 500
HEIGHT = 500

alan = Sprite('alien.png')
alan.pos = (200, 200)

def draw():
    alan.draw()

def update():
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2
    if keyboard.space:
        schedule_cancel(animateAlien)

images = ["alien_hurt.png", "alien.png"]
image_counter = 0

def animateAlien():
    global image_counter
    alan.image_file = images[image_counter % len(images)]
    image_counter += 1

schedule_repeat(animateAlien, 0.2)

run()