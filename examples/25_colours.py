from rlzero import *

# my_colour = Color(0,0,0,255) # makes black
# my_colour = Color(255,255,255,255) # makes white

red_amount = 0
green_amount = 0
blue_amount = 0
alpha_amount = 255

def draw():
    my_colour = Color(red_amount, green_amount, blue_amount, alpha_amount)
    clear_background(my_colour)

# This function makes the colour change every frame
# Remove it if you just want to see a static colour.
def update():
    global red_amount
    red_amount += 1
    red_amount = red_amount % 255

run()