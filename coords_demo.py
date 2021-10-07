from rlzero import *


WIDTH=1200
HEIGHT=800
CAMERA=pr.CAMERA_FIRST_PERSON


player = Box((-5, 0, -5), (1, 1, 1), 'green', True)


o = Vector([-5,-0,-5])

td = False


def init():
    camera.position = (0.0, 4, 7)
    camera.target = (100,100,-100)
    camera.up = (0, 1, 0)
    camera.fovy = 60
    #rl.UpdateCamera(camera)
    pr.set_camera_mode(camera[0], pr.CAMERA_FIRST_PERSON)
    #rl.UpdateCamera(camera)

def update():
    if keyboard.right:
        player.pos.x += 0.1
    elif keyboard.left:
        player.pos.x -= 0.1
    elif keyboard.up:
        player.pos.y += 0.1
    elif keyboard.down:
        player.pos.y -= 0.1
    elif keyboard.l:
        player.pos.z += 0.1
    elif keyboard.p:
        player.pos.z-= 0.1

    if pr.is_key_pressed(pr.KEY_Z):
        global td
        td = not td


def draw3d():
    if td:
        #pyray.draw_plane((0, 0, 0), (300,300), DARKRED)
        pr.draw_grid(10, 1)
        pr.draw_plane((player.x, 0, player.z), (1, 1), GRAY)
        pr.draw_ray([o, [0, 0, 1]], BLUE)
    pr.draw_ray([o, [0, 1, 0]], GREEN)
    pr.draw_ray([o, [1, 0, 0]], RED)
    player.draw()


def draw2dbackground():
    clear('white')
    origin = rl.GetWorldToScreen(o,  camera[0])
    rl.DrawText(b"0", int(origin.x), int(origin.y), 20, BLACK)
    for i in range (0,11):
        xa = rl.GetWorldToScreen((o.x+i,o.y,o.z),  camera[0])
        ya = rl.GetWorldToScreen((o.x,o.y+i,o.z),  camera[0])
        za = rl.GetWorldToScreen((o.x,o.y,o.z+i),  camera[0])
        pr.draw_text(str(i), int(xa.x), int(xa.y), 20, RED)
        pr.draw_text(str(i), int(ya.x), int(ya.y), 20, GREEN)
        if td:
            pr.draw_text(str(i), int(za.x), int(za.y), 20, BLUE)

    pr.draw_text(f"X: {int(player.x + 5)}", 10, 10, 30, RED)
    pr.draw_text(f"Y: {int(player.y)}", 10, 50, 30, GREEN)
    if td:
        pr.draw_text(f"Z: {int(player.z + 5)}", 10, 110, 30, BLUE)



run()
