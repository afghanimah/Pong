import pyglet
from pyglet.window import key
from entity import Entity
import utils
import random
from scene import Scene


# PyCharm bug:
# noinspection PyAbstractClass
class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__()
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
