from raylib.pyray import PyRay


rl = PyRay()

WIDTH = 1920
HEIGHT = 1080

# Plot window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

MAX_ITER = 80

palette = []

rl.init_window(WIDTH, HEIGHT, "Mandlebrot")
rl.set_target_fps(60)

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    return n


def draw():
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                        IM_START + (y / HEIGHT) * (IM_END - IM_START))
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
            rl.draw_pixel(x, y, color)


while not rl.window_should_close():
    rl.begin_drawing()
    draw()
    rl.end_drawing()


