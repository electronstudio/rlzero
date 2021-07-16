from rlzero import *


#WIDTH=200
#HEIGHT=200
CAMERA=rl.CAMERA_FIRST_PERSON
#DATA_DIR="examples/models/resources/models/"
#DATA_DIR="/Volumes/Home/rich/vulcan/"

sound = Sound('eep')
sound.volume = 0.7
sound.pitch = 0.5

player = Cube((0, 10, 20), (10, 20, 10), 'green')
enemy_box = Cube((-40, 10, 0), (20, 20, 20), (150,0,0))
enemy_sphere = Sphere((40, 15, 0), 15, 'gray')
castle = Actor("castle", collision_radius=15, wires=False)
castle.z=-50
castle.x=0
castle.size.y=1
castle.size.x=1
castle.size.z=1

bob = Actor("test", collision_radius=20, wires=True, color=GREEN)
bob.z=-100
bob.x=50
bob.y=-50
bob.pos = (50,25,-100)


#def init():
    #global lights0

lightSystem = getLightSystem()
lights0 = Light([ 30, 30, 30 ], Vector([0,0,0]))
lightSystem.add(lights0)


def update():
    update_player()
    update_bob()
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

    if enemy_box.check_collision(player) or enemy_sphere.check_collision(player) or castle.check_collision(player) or bob.check_collision(player):
        player.color = 'red'
        sound.play()
    else:
        player.color = 'green'

    lights0.pos = player.pos

def update_sphere():
    #gamepad.test()
    #gamepad1.test()
    print(gamepad.left_stick.x)
    if gamepad.left_stick.x > 0.3:
        enemy_sphere.pos.x += 2
    elif gamepad.left_stick.x < -0.3:
        enemy_sphere.pos.x -= 2
    elif gamepad.left_stick.y > 0.3:
        enemy_sphere.pos.z += 2
    elif gamepad.left_stick.y < -0.3:
        enemy_sphere.pos.z -= 2

    if enemy_box.check_collision(enemy_sphere) or player.check_collision(enemy_sphere) or castle.check_collision(enemy_sphere) or bob.check_collision(enemy_sphere):
        enemy_sphere.color = 'red'
    else:
        enemy_sphere.color = 'green'


def update_bob():
    if keyboard.d:
        bob.pos.x += 2
    elif keyboard.a:
        bob.pos.x -= 2
    elif keyboard.s:
        bob.pos.z += 2
    elif keyboard.w:
        bob.pos.z -= 2

    if enemy_box.check_collision(bob) or enemy_sphere.check_collision(bob) or castle.check_collision(bob) or player.check_collision(bob):
        bob.color = 'red'
    else:
        bob.color = 'green'




def draw3d():
    clear('white')
    enemy_box.draw()
    enemy_sphere.draw()
    player.draw()
    castle.draw()
    bob.draw()


def draw2d():
    screen.draw_text("Move player with cursors to collide", 220, 40, 20, (255,0,0,255))
    pyray.draw_fps(20,20)


run()
