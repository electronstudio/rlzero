from rlzero import *
import random
import math

WIDTH = 600
HEIGHT = 800

player = Sprite("alien.png", (300, 750))
player.vx = 0   # horizontal velocity
player.vy = 1   # vertical velocity

lines = []          # list of tuples of horizontal lines of walls
wall_gradient = -3  # steepness of wall
left_wall_x = 200   # x-coordinate of wall
distance = 0        # how far player has travelled
time = 15           # time left until game ends
playing = False     # True when in game, False when on title screen
best_distance = 0   # remember the highest distance scored

def draw():
    if playing: # we are in game
        for i in range(0, len(lines)): # draw the walls
            x, x2, color = lines[i]
            draw_line(0, i, int(x), i, color)
            draw_line(int(x + x2), i, WIDTH, i, color)
        player.draw()
    else:   # we are on title screen
        draw_text("PRESS SPACE TO START", 150, 300, 30, GREEN)
        draw_text("BEST DISTANCE: "+str(int(best_distance / 10)),
            170, 400,  30, GREEN)
    draw_text("SPEED: " + str(int(player.vy)),
        0, 0, 30, GREEN)
    draw_text("DISTANCE: " + str(int(distance / 10)),
        200, 0, 30, GREEN)
    draw_text("TIME: " + str(int(time)),
        480, 0, 30, GREEN)


def update(delta):
    global playing, distance, time
    if playing:
        wall_collisions()
        scroll_walls()
        generate_lines()
        player_input()
        timer(delta)
    elif keyboard.space:
        playing = True
        distance = 0
        time = 10


def player_input():
    if keyboard.up:
        player.vy += 0.1
    if keyboard.down:
        player.vy -= 0.1
        if player.vy < 1:
            player.vy = 1
    if keyboard.right:
        player.vx += 0.4
    if keyboard.left:
        player.vx -= 0.4
    player.x += player.vx

def generate_lines():
    global wall_gradient, left_wall_x
    gap_width = 300 + math.sin(distance / 3000) * 100
    while len(lines) < HEIGHT:
        pretty_colour = Color(255, int(min(left_wall_x, 255)), int(min(time * 5, 255)), 255)
        lines.insert(0, (left_wall_x, gap_width, pretty_colour))
        left_wall_x += wall_gradient
        if left_wall_x < 0:
            left_wall_x = 0
            wall_gradient = random.random() * 2 + 0.1
        elif left_wall_x + gap_width > WIDTH:
            left_wall_x = WIDTH - gap_width
            wall_gradient = -random.random() * 2 - 0.1

generate_lines()

def scroll_walls():
    global distance
    for i in range(0, int(player.vy)):
        lines.pop()
        distance += 1

def wall_collisions():
    a, b, c = lines[-1]
    if player.x < a:
        player.x += 5
        player.vx = player.vx * -0.5
        player.vy = 0
    if player.x + 50 > a + b:
        player.x -= 5
        player.vx = player.vx * -0.5
        player.vy = 0

def timer(delta):
    global time, playing, best_distance
    time -= delta
    if time < 0:
        playing = False
        if distance > best_distance:
            best_distance = distance

def on_mouse_move(pos):
    x, y = pos
    player.x = x
    player.vy = (HEIGHT - y) / 20

run()