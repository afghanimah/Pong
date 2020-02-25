import pyglet
from pyglet.window import key
from entity import Entity
import utils
import random


class Game(pyglet.window.Window):
    def __init__(self):
        super(Game, self).__init__()
        self.paddle_img = utils.load_image("paddle.png")
        self.ball_img = utils.load_image("ball.png")
        self.player = Entity(self.paddle_img, 20, (self.height - self.paddle_img.height) / 2, 250)
        self.cpu = Entity(self.paddle_img, self.width - self.paddle_img.width - 20,
                          (self.height - self.paddle_img.height) / 2, 250)
        self.ball = Entity(self.ball_img, (self.width - self.ball_img.width) / 2,
                           (self.height - self.ball_img.height) / 2, 500)
        self.ball.vx = 300
        self.ball.vy = 300
        self.player_score = 0
        self.cpu_score = 0
        self.player_label = pyglet.text.Label(str(self.player_score),
                                              font_name='Ubuntu',
                                              font_size=64,
                                              x=self.width / 3,
                                              y=self.height - 50,
                                              anchor_x='center', anchor_y='center')
        self.colon = pyglet.text.Label(":",
                                       font_name='Ubuntu',
                                       font_size=64,
                                       x=self.width / 2,
                                       y=self.height - 40,
                                       anchor_x='center', anchor_y='center')
        self.cpu_label = pyglet.text.Label(str(self.cpu_score),
                                           font_name='Ubuntu',
                                           font_size=64,
                                           x=2 * self.width / 3,
                                           y=self.height - 50,
                                           anchor_x='center', anchor_y='center')
        self.pause_label = pyglet.text.Label("pause",
                                             font_name='Ubuntu',
                                             font_size=64,
                                             x=self.width / 2,
                                             y=self.height / 2,
                                             anchor_x='center', anchor_y='center')
        self.paused = False
        self.hit_sound = utils.load_sound("button-10.wav", streaming=False)
        self.point_sound = utils.load_sound("point.wav", streaming=False)

    def update(self, dt):
        if self.paused:
            return
        self.player.update(dt)
        self.cpu.follow(self.ball.sprite.x + self.ball.sprite.width / 2,
                        self.ball.sprite.y + self.ball.sprite.height / 2)
        self.cpu.update(dt)
        self.ball.update(dt)
        self.window_bound()
        self.bounce_ball()

    def on_draw(self):
        self.clear()
        self.player.draw()
        self.cpu.draw()
        self.ball.draw()
        self.player_label.draw()
        self.cpu_label.draw()
        self.colon.draw()
        if self.paused:
            self.pause_label.draw()

    def on_key_press(self, symbol, modifiers):
        self.player.key_down(symbol, modifiers)
        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.SPACE:
            self.paused = not self.paused

    def on_key_release(self, symbol, modifiers):
        self.player.key_up(symbol, modifiers)

    def bound_x(self, e, min, max):
        if e.sprite.x < min:
            e.sprite.x = min
        elif e.sprite.x > max:
            e.sprite.x = max

    def bound_y(self, e, min, max):
        if e.sprite.y < min:
            e.sprite.y = min
        elif e.sprite.y > max:
            e.sprite.y = max

    def window_bound(self):
        self.bound_x(self.player, 0, self.width - self.player.sprite.width)
        self.bound_y(self.player, 0, self.height - self.player.sprite.height)
        self.bound_x(self.cpu, 0, self.width - self.player.sprite.width)
        self.bound_y(self.cpu, 0, self.height - self.player.sprite.height)

    def bounce_ball(self):
        x_min = 0
        x_max = self.width - self.ball.sprite.width
        y_min = 0
        y_max = self.height - self.ball.sprite.height

        if self.ball.sprite.y < y_min:
            self.ball.sprite.y = y_min
            self.ball.vy *= -1
            self.hit_sound.play()
        elif self.ball.sprite.y > y_max:
            self.ball.sprite.y = y_max
            self.ball.vy *= -1
            self.hit_sound.play()

        if self.ball.sprite.x < x_min:
            self.ball.sprite.x = (self.width - self.ball_img.width) / 2 - 200
            self.ball.sprite.y = (self.height - self.ball_img.height) / 2
            self.ball.vx = random.randint(300, 350)
            self.ball.vy = random.randint(300, 350) * (-1 if random.randint(0, 1) == 0 else 1)
            self.cpu_score += 1
            self.cpu_label.text = str(self.cpu_score)
            self.point_sound.play()
        elif self.ball.sprite.x > x_max:
            self.ball.sprite.x = (self.width - self.ball_img.width) / 2 + 200
            self.ball.sprite.y = (self.height - self.ball_img.height) / 2
            self.ball.vx = -random.randint(300, 350)
            self.ball.vy = -random.randint(300, 350) * (-1 if random.randint(0, 1) == 0 else 1)
            self.player_score += 1
            self.player_label.text = str(self.player_score)
            self.point_sound.play()

        if (self.player.sprite.x + self.player.sprite.width / 2 < self.ball.sprite.x + self.ball.sprite.width / 2 < self.player.sprite.x + self.player.sprite.width and
            self.player.sprite.y + self.player.sprite.height > self.ball.sprite.y + self.ball.sprite.height / 2 > self.player.sprite.y):
            self.ball.sprite.x = self.player.sprite.x + self.player.sprite.width
            self.ball.vx *= -1
            self.hit_sound.play()
        elif (self.cpu.sprite.x < self.ball.sprite.x + self.ball.sprite.width / 2 < self.cpu.sprite.x + self.cpu.sprite.width / 2 and
            self.cpu.sprite.y + self.cpu.sprite.height > self.ball.sprite.y + self.ball.sprite.height / 2 > self.cpu.sprite.y):
            self.ball.sprite.x = self.cpu.sprite.x - self.ball.sprite.width
            self.ball.vx *= -1
            self.hit_sound.play()
