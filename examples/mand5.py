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
            c = complex((RE_START + (x / WIDTH) * RE_WIDTH),
                        (IM_START + (y / HEIGHT) * IM_HEIGHT))
            m = mandelbrot(c)
            i = 255 - int(255 * m / MAX_ITER)
            color = (i, i, i, 255)
            screen.draw_pixel(x, y, color)


run()
