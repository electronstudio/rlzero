from rlzero import *
from rlzero.rlights import Light

WIDTH=500
HEIGHT=500
CAMERA=rl.CAMERA_FIRST_PERSON
DATA_DIR="examples/data"


sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5

player = Cube((0, 10, 20), (10, 20, 10), 'green')
enemy_box = Cube((-40, 10, 0), (20, 20, 20), (150,0,0))
enemy_sphere = Sphere((40, 15, 0), 15, 'gray')
dragon = Model("monsters/Dragon", collision_radius=15, wires=False)
dragon.z=-50
dragon.x=0
dragon.size.y=10
dragon.size.x=10
dragon.size.z=10

wiz = Model("rpg_characters/Wizard", collision_radius=20, wires=False, color=GREEN)
wiz.z=-100
wiz.x=50
wiz.y=-50
wiz.size = (10,10,10)
wiz.pos = (50,25,-100)


#def init():
    #global lights0

lightSystem = getLightSystem()
lights0 = Light([ 30, 30, 30 ], Vector([0,0,0]))
lightSystem.add(lights0)


def update():
    update_player()
    update_wiz()
    update_sphere()

def update_player():
    if keyboard.right:
        player.pos.x += 2
    elif keyboard.left:
        player.pos.x -= 2
    elif keyboard.down:
        player.pos.z += 2
    elif keyboard.up:
        player.pos.z -= 2

    if enemy_box.check_collision(player) or enemy_sphere.check_collision(player) or dragon.check_collision(player) or wiz.check_collision(player):
        player.color = 'red'
        sound.play()
    else:
        player.color = 'green'

    lights0.pos = player.pos

def update_sphere():
    #gamepad.test()
    #gamepad1.test()
    #print(gamepad.left_stick.x)
    if gamepad.left_stick.x > 0.3:
        enemy_sphere.pos.x += 2
    elif gamepad.left_stick.x < -0.3:
        enemy_sphere.pos.x -= 2
    elif gamepad.left_stick.y > 0.3:
        enemy_sphere.pos.z += 2
    elif gamepad.left_stick.y < -0.3:
        enemy_sphere.pos.z -= 2

    if enemy_box.check_collision(enemy_sphere) or player.check_collision(enemy_sphere) or dragon.check_collision(enemy_sphere) or wiz.check_collision(enemy_sphere):
        enemy_sphere.color = 'red'
    else:
        enemy_sphere.color = 'green'


def update_wiz():
    if keyboard.d:
        wiz.pos.x += 2
    elif keyboard.a:
        wiz.pos.x -= 2
    elif keyboard.s:
        wiz.pos.z += 2
    elif keyboard.w:
        wiz.pos.z -= 2

    if enemy_box.check_collision(wiz) or enemy_sphere.check_collision(wiz) or dragon.check_collision(wiz) or player.check_collision(wiz):
        wiz.color = 'red'
    else:
        wiz.color = 'green'




def draw3d():
    clear('white')
    enemy_box.draw()
    enemy_sphere.draw()
    player.draw()
    dragon.draw()
    wiz.draw()


def draw2d():
    screen.draw_text("Move player with cursors to collide", 220, 40, 20, (255,0,0,255))
    pr.draw_fps(20, 20)



run()