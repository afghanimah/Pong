import pyglet
from pyglet.window import key
from scene import Scene
from resourcemanager import ResourceManager


# PyCharm bug:
# noinspection PyAbstractClass
class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__()
        self.resources = ResourceManager()
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        self.scene = Scene(self)

    def update(self, dt):
        self.scene.update(dt)

    def on_draw(self):
        self.clear()
        self.scene.draw()

    def on_key_press(self, symbol, modifiers):
        self.scene.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.scene.on_key_release(symbol, modifiers)
