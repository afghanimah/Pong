import pyglet
from paddle import Paddle
from ball import Ball
from pongcontroller import PongController
from scene import Scene
from resourcemanager import ResourceManager


class PongScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.width = game.width
        self.height = game.height
        self.close = game.close
        self.keys = game.keys
        self.resources = ResourceManager()
        self.paddle_img = self.resources.load_image("paddle")
        self.ball_img = self.resources.load_image("ball")
        self.player = Paddle(self.paddle_img, 20 + self.paddle_img.anchor_x, self.height / 2, 250, self.batch)
        self.cpu = Paddle(self.paddle_img, self.width - self.paddle_img.anchor_x - 20, self.height / 2, 250, self.batch)
        self.ball = Ball(self.ball_img, self.width / 2, self.height / 2, 300, self.batch)
        self.ball.vx = self.ball.speed
        self.ball.vy = self.ball.speed
        self.player_score = 0
        self.cpu_score = 0
        self.player_label = pyglet.text.Label(str(self.player_score),
                                              font_name='Ubuntu',
                                              font_size=64,
                                              x=self.width / 3,
                                              y=self.height - 50,
                                              anchor_x='center', anchor_y='center', batch=self.batch)
        self.colon = pyglet.text.Label(":",
                                       font_name='Ubuntu',
                                       font_size=64,
                                       x=self.width / 2,
                                       y=self.height - 40,
                                       anchor_x='center', anchor_y='center', batch=self.batch)
        self.cpu_label = pyglet.text.Label(str(self.cpu_score),
                                           font_name='Ubuntu',
                                           font_size=64,
                                           x=2 * self.width / 3,
                                           y=self.height - 50,
                                           anchor_x='center', anchor_y='center', batch=self.batch)
        self.pause_label = pyglet.text.Label("pause",
                                             font_name='Ubuntu',
                                             font_size=64,
                                             x=self.width / 2,
                                             y=self.height / 2,
                                             anchor_x='center', anchor_y='center')
        self.paused = False
        self.hit_sound = self.resources.load_sound("button-10")
        self.point_sound = self.resources.load_sound("point")
        self.controllers.append(PongController(self))

    def draw(self):
        super().draw()
        if self.paused:
            self.pause_label.draw()
