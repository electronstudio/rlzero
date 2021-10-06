from rlzero import *

alien = Sprite("alien")
alien.pos = (0, 50)
eep = Sound("eep")

score = 0

def draw():
    clear()
    alien.draw()
    draw_text("Score "+str(score), 0, 0, 20, WHITE)

def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    alien.image = 'alien'

def on_mouse_down(pos, button):
    global score
    if button == pyray.MOUSE_LEFT_BUTTON and alien.collidepoint(pos):
        alien.image = 'alien_hurt'
        eep.play()
        score = score + 1

run()

