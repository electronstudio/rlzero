from rlzero import *

WIDTH = 500
HEIGHT = 500

aliens = []
for i in range(0,10):
    aliens.append(Sprite('alien.png', (i*30, i*30)))

def draw():
    for alien in aliens:
        alien.draw()

def update():
    for alien in aliens:
        alien.x += 2
        if alien.x > WIDTH:
            alien.x = 0

def on_mouse_pressed(pos, button):
    aliens.append(Sprite('alien.png', pos))

run()