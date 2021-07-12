from rlzero import *


#WIDTH=800
#HEIGHT=640
#CAMERA=rl.CAMERA_FIRST_PERSON
#DATA_DIR="examples/models/resources/models/"
#DATA_DIR="/Volumes/Home/rich/vulcan/"

player = Cube((0, 10, 20), (10, 20, 10), 'green')
enemy_box = Cube((-40, 10, 0), (20, 20, 20), (150,0,0))
enemy_sphere = Sphere((40, 15, 0), 15, 'gray')
castle = Actor("castle", collision_radius=15)
castle.z=-50
castle.x=0
castle.size.y=1
castle.size.x=1
castle.size.z=1

bob = Actor("test", collision_radius=20, wires=True, color=GREEN)
bob.z=-100
bob.x=50


def init():
    global lights0
    lightSystem = getLightSystem()
    lights0 = Light([ 30, 30, 30 ], Vector([0,0,0]))
    lightSystem.add(lights0)


def update():
    if keyboard.right:
        player.pos.x += 2
    elif keyboard.left:
        player.pos.x -= 2
    elif keyboard.down:
        player.pos.z += 2
    elif keyboard.up:
        player.pos.z -= 2

    #if player.check_collision(enemy_box) or player.check_collision(enemy_sphere) or player.check_collision(castle) or player.check_collision(bob):
    if enemy_box.check_collision(player) or enemy_sphere.check_collision(player) or castle.check_collision(player) or bob.check_collision(player):
        player.color = 'red'
    else:
        player.color = 'green'

    lights0.pos = player.pos



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
