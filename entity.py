import pyglet


class Entity:
    def __init__(self, img, x, y, speed, batch):
        self.sprite = pyglet.sprite.Sprite(img, x, y, batch=batch)
        self.vx = 0
        self.vy = 0
        self.speed = speed

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
