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


def plot_image():
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            c = complex((RE_START + (x / WIDTH) * RE_WIDTH),
                        (IM_START + (y / HEIGHT) * IM_HEIGHT))
            m = mandelbrot(c)
            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            color = pyray.color_from_hsv(hue, saturation, value)
            screen.image_draw_pixel(image, x, y, color)


image = screen.gen_image_color(WIDTH, HEIGHT, GREEN)
plot_image()


def init():
    global texture
    texture = screen.load_texture_from_image(image)
    screen.set_texture_filter(texture, screen.TEXTURE_FILTER_BILINEAR)


def draw2d():
    screen.draw_texture_ex(texture, (0, 0), 0, 1, WHITE)


run()
