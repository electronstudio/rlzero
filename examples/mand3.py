from rlzero import *

WIDTH = 1920
HEIGHT = 1080

RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

RE_WIDTH = (RE_END - RE_START)
IM_HEIGHT = (IM_END - IM_START)

MAX_ITER = 80

zoom = 1.0

SCALE = 4




def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def plot_image():
    for x in range(0, WIDTH//SCALE):
        for y in range(0, HEIGHT//SCALE):
            # Convert pixel coordinate to complex number
            c = complex((RE_START + (x / (WIDTH//SCALE)) * RE_WIDTH) * zoom,
                        (IM_START + (y / (HEIGHT//SCALE)) * IM_HEIGHT) * zoom)
            # Compute the number of iterations
            m = mandelbrot(c)
            # The color depends on the number of iterations
            bw = 255 - int(m * 255 / MAX_ITER)
            color = (bw, bw, bw, 255)

            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            color = pyray.color_from_hsv(hue, saturation, value)

            # Plot the point
            pyray.image_draw_pixel(image, x, y, color)



image = pyray.gen_image_color(WIDTH, HEIGHT, GREEN)
plot_image()


def init():
    global texture
    texture = pyray.load_texture_from_image(image)
    pyray.set_texture_filter(texture, pyray.TEXTURE_FILTER_BILINEAR)



def draw2d():
    pyray.draw_texture_ex(texture, (0,0), 0, SCALE, WHITE)


def update():
    global zoom, IM_START, RE_START
    rl.UpdateTexture(texture, image.data)
    if keyboard.space:
        zoom = zoom * 1.2
        plot_image()
    elif keyboard.enter:
        zoom = zoom * 0.8
        plot_image()
    elif keyboard.up:
        IM_START -= 0.2
        plot_image()
    elif keyboard.down:
        IM_START += 0.2
        plot_image()
    elif keyboard.left:
        RE_START -= 0.2
        plot_image()
    elif keyboard.right:
        RE_START += 0.2
        plot_image()

run()

