from rlzero import *

timer = 0

def update(dt):
    global timer
    timer += dt


def draw():
    clear()
    draw_text(f"Time passed: {timer}", 0, 0, 20, RED)
    if timer > 5:
        draw_text("Time's up!", 50, 50, 40, WHITE)

run()