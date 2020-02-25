import pyglet
from pyglet.window import key


class Entity:
    def __init__(self, img, x, y, speed, batch):
        self.sprite = pyglet.sprite.Sprite(img, x, y, batch=batch)
        self.vx = 0
        self.vy = 0
        self.speed = speed

    def key_down(self, symbol, modifiers):
        if symbol == key.UP:
            self.vy += self.speed
        elif symbol == key.DOWN:
            self.vy -= self.speed

    def key_up(self, symbol, modifiers):
        if symbol == key.UP:
            self.vy -= self.speed
        elif symbol == key.DOWN:
            self.vy += self.speed

    def follow(self, x, y):
        if self.sprite.y < y:
            self.vy = self.speed
        elif self.sprite.y > y:
            self.vy = -self.speed

    def update(self, dt):
        self.sprite.x += self.vx * dt
        self.sprite.y += self.vy * dt

    def draw(self):
        self.sprite.draw()
