from rlzero import *

WIDTH = 500
HEIGHT = 500
alien = Sprite("alien")
animation = Animation(["alien", "alien_hurt"])
alien.pos = (0, 50)
box = Rectangle(20, 20, 100, 100)
eep = Sound("eep")

def draw():
    clear()
    draw_rectangle_rec(box, RED)
    alien.draw()
def update():
    if keyboard.right:
        alien.x = alien.x + 2
    elif keyboard.left:
        alien.x = alien.x - 2
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
# PLAY SOUND AND SHOW IMAGE WHEN HIT
    if alien.colliderect(box):
        alien.texture = animation.get_texture(1)
        eep.play()
    else:
        alien.texture = animation.get_texture(0)

run()