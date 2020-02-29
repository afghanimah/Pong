import pyglet


class Entity:
    def __init__(self, img, x, y, batch):
        self.sprite = pyglet.sprite.Sprite(img, x, y, batch=batch)

    def update(self, dt):
        pass

    def draw(self):
        self.sprite.draw()
