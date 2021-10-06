from raylib.pyray import PyRay
from raylib import *
# from math import log, log2
import threading

rl = PyRay()

WIDTH = 1920
HEIGHT = 1080

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

RE_WIDTH = (RE_END - RE_START)
IM_HEIGHT = (IM_END - IM_START)

MAX_ITER = 80

zoom = 1.0

scale = 4

palette = []

rl.init_window(WIDTH, HEIGHT, "Mandlebrot")
rl.set_target_fps(60)

image = rl.gen_image_color(WIDTH, HEIGHT, (0,0,0,255) )
texture = rl.load_texture_from_image(image)
rl.set_texture_filter(texture, TEXTURE_FILTER_BILINEAR)

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n
    #if n == MAX_ITER:
    #    return MAX_ITER

    #return n + 1 - log(log2(abs(z)))

stop = False

def draw():
    for x in range(0, WIDTH//scale):
        for y in range(0, HEIGHT//scale):
            # Convert pixel coordinate to complex number
            c = complex((RE_START + (x / (WIDTH//scale)) * (RE_WIDTH))*zoom,
                        (IM_START + (y / (HEIGHT//scale)) * (IM_HEIGHT))*zoom)
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations
            bw = 255 - int(m * 255 / MAX_ITER)
            color = (bw, bw, bw, 255)

            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            color = rl.color_from_hsv(hue, saturation, value)

            # Plot the point
            rl.image_draw_pixel(image, x, y, color)
            if stop:
                return


def redraw():
    draw()
    # global thread
    # stop = True
    # thread.join()
    # stop = False
    # thread = threading.Thread(target=draw)
    # thread.start()

thread = threading.Thread(target=draw)
thread.start()

draw()

while not rl.window_should_close():
    rl.begin_drawing()

    UpdateTexture(texture, image.data)
    #rl.update_texture(texture, image.data[0])
    #rl.draw_texture(texture, 0, 0, (255,255,255,255))
    rl.draw_texture_ex(texture, (0,0), 0, scale, (255,255,255,255))
    rl.end_drawing()

    if rl.is_key_pressed(KEY_SPACE):
        zoom = zoom * 1.2
        redraw()
    elif rl.is_key_pressed(KEY_ENTER):
        zoom = zoom * 0.8
        redraw()
    elif rl.is_key_pressed(KEY_UP):
        IM_START -= 0.2
        redraw()
    elif rl.is_key_pressed(KEY_DOWN):
        IM_START += 0.2
        redraw()
    elif rl.is_key_pressed(KEY_LEFT):
        RE_START -= 0.2
        redraw()
    elif rl.is_key_pressed(KEY_RIGHT):
        RE_START += 0.2
        redraw()
    elif rl.is_key_pressed(KEY_Z):
        scale = 1
        redraw()
    elif rl.is_key_pressed(KEY_X):
        scale = 4
        redraw()

