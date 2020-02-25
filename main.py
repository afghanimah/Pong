import pyglet
from game import Game

pyglet.resource.path = ['resources/']
pyglet.resource.reindex()
window = Game()
pyglet.clock.schedule_interval(window.update, 1/120.0)
pyglet.app.run()