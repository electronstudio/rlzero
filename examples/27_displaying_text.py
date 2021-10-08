from rlzero import *

WIDTH = 500
HEIGHT = 500

score = 0

def draw():
    clear()
    draw_text(f"Player 1 score: {score}", 0, 0, 20, RED)

# This is another special function that is called by RLzero automatically
# each time a key is pressed. That way player cannot just hold down the key!

def on_key_pressed(key):
    global score
    if key == KEY_SPACE:
        score += 1

run()