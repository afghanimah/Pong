import pyglet


class Scene:
    def __init__(self, game):
        self.game = game
        self.batch = pyglet.graphics.Batch()
        self.controllers = []

    def controller(self):
        return self.controllers[-1]

    def update(self, dt):
        self.controller().update(dt)

    def draw(self):
        self.batch.draw()

    def on_key_press(self, symbol, modifiers):
        self.controller().on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.controller().on_key_release(symbol, modifiers)
