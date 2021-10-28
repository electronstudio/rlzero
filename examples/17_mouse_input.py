from rlzero import *

alan = Sprite("alien.png")
alan.pos = (0, 50)
eep = Sound("eep")

score = 0

def draw():
    alan.draw()
    draw_text("Score "+str(score), 0, 0, 20, WHITE)

def update():
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2
    alan.image = 'alien.png'

def on_mouse_down(pos, button):
    global score
    if button == MOUSE_LEFT_BUTTON and alan.collidepoint(pos):
        alan.image = 'alien_hurt.png'
        eep.play()
        score = score + 1

run()

