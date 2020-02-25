import pyglet
from game import Game

window = Game()
pyglet.clock.schedule_interval(window.update, 1/120.0)
pyglet.app.run()