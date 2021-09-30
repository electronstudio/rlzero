from rlzero import *

WIDTH = 700
HEIGHT = 400
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1
RE_WIDTH = (RE_END - RE_START)
IM_HEIGHT = (IM_END - IM_START)
MAX_ITER = 80

zoom = 1.0


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n


def draw2d():
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            c = complex((RE_START + (x / WIDTH) * RE_WIDTH) * zoom,
                        (IM_START + (y / HEIGHT) * IM_HEIGHT) * zoom)
            m = mandelbrot(c)
            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            color = screen.color_from_hsv(hue, saturation, value)
            screen.draw_pixel(x, y, color)


def update():
    global zoom, IM_START, RE_START
    if keyboard.space:
        zoom *= 1.2
    elif keyboard.enter:
        zoom *= 0.8
    elif keyboard.up:
        IM_START -= 0.2
    elif keyboard.down:
        IM_START += 0.2
    elif keyboard.left:
        RE_START -= 0.2
    elif keyboard.right:
        RE_START += 0.2


run()
