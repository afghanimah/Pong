import pyglet
from game import Game

if __name__ == "__main__":
    window = Game()
    pyglet.clock.schedule_interval(window.update, 1/120.0)
    pyglet.app.run()
