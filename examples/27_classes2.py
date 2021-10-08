from rlzero import *

WIDTH = 500
HEIGHT = 500

class MySprite(Sprite):
    vx = 1
    vy = 1

    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > WIDTH or self.x < 0:
            self.vx = -self.vx
        if self.y > HEIGHT or self.y < 0:
            self.vy = -self.vy

ball = MySprite("alien.png")

def draw():
    clear()
    ball.draw()

def update():
    ball.update()

run()