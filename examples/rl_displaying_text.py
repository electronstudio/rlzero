"""
Simple game that displays text on screen
Note that text is 2d, not 3d, so it must be drawn in draw2d() function
"""

from rlzero import *

score = 0

def draw():
    clear()

def draw2d():
    pyray.draw_text(f"Player 1 score: {score}", 0, 0, 40, VIOLET)

def update():
    global score
    if keyboard.key_pressed('space'):
        score += 1

run()


"""
TODO
Make the score text larger and RED colored
Add score2 for player 2 that increases when P key is pressed
Add score display to another program, e.g. 17
"""