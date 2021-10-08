from rlzero import *

WIDTH = 500
HEIGHT = 500
alan = Sprite("alien.png")
tex1 = Texture("alien.png")
tex2 = Texture("alien_hurt.png")
alan.pos = (0, 50)
box = Rectangle(20, 20, 100, 100)
eep = Sound("eep")

def draw():
    clear()
    draw_rectangle_rec(box, RED)
    alan.draw()
def update():
    if keyboard.right:
        alan.x = alan.x + 2
    elif keyboard.left:
        alan.x = alan.x - 2
    box.x = box.x + 2
    if box.x > WIDTH:
        box.x = 0
# PLAY SOUND AND SHOW IMAGE WHEN HIT
    if alan.colliderect(box):
        alan.texture = tex2
        eep.play()
    else:
        alan.texture = tex1

run()