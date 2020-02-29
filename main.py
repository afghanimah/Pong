import pyglet
from game import Game
from pongscene import PongScene

if __name__ == "__main__":
    window = Game()
    window.scenes.append(PongScene(window))
    pyglet.clock.schedule_interval(window.update, 1/120.0)
    pyglet.app.run()
