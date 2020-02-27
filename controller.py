import pyglet
from pyglet.window import key
from entity import Entity
import utils
import random


class Controller:
    def __init__(self, scene):
        self.scene = scene
        self.keys = scene.keys
        self.player = scene.player
        self.cpu = scene.cpu
        self.ball = scene.ball
        self.close = scene.close

    def update(self, dt):
        if self.scene.paused:
            return
        self.player.update(dt)
        self.cpu.follow(self.ball.sprite.x, self.ball.sprite.y)
        self.cpu.update(dt)
        self.ball.update(dt)
        self.window_bound()
        self.bounce_ball()

    def on_key_press(self, symbol, modifiers):
        self.player.key_down(symbol, modifiers)
        if symbol == key.ESCAPE:
            self.close()
        if symbol == key.SPACE:
            self.scene.paused = not self.scene.paused

    def on_key_release(self, symbol, modifiers):
        self.player.key_up(symbol, modifiers)

    @staticmethod
    def bound_x(e, mini, maxi):
        mini += e.sprite.width / 2
        maxi -= e.sprite.width / 2
        if e.sprite.x < mini:
            e.sprite.x = mini
        elif e.sprite.x > maxi:
            e.sprite.x = maxi

    @staticmethod
    def bound_y(e, mini, maxi):
        mini += e.sprite.height / 2
        maxi -= e.sprite.height / 2
        if e.sprite.y < mini:
            e.sprite.y = mini
        elif e.sprite.y > maxi:
            e.sprite.y = maxi

    def window_bound(self):
        self.bound_x(self.player, 0, self.scene.width)
        self.bound_y(self.player, 0, self.scene.height)
        self.bound_x(self.cpu, 0, self.scene.width)
        self.bound_y(self.cpu, 0, self.scene.height)

    def bounce_ball(self):
        x_min = self.scene.ball_img.anchor_x
        x_max = self.scene.width - self.scene.ball_img.anchor_x
        y_min = self.scene.ball_img.anchor_y
        y_max = self.scene.height - self.scene.ball_img.anchor_y

        if self.ball.sprite.y < y_min:
            self.ball.sprite.y = y_min
            self.ball.vy *= -1
            self.scene.hit_sound.play()
        elif self.ball.sprite.y > y_max:
            self.ball.sprite.y = y_max
            self.ball.vy *= -1
            self.scene.hit_sound.play()

        if self.ball.sprite.x < x_min:
            self.ball.sprite.x = self.scene.width / 2 - 200
            self.ball.sprite.y = self.scene.height / 2
            self.ball.vx = random.randint(300, 350)
            self.ball.vy = random.randint(300, 350) * (-1 if random.randint(0, 1) == 0 else 1)
            self.scene.cpu_score += 1
            self.scene.cpu_label.text = str(self.scene.cpu_score)
            self.scene.point_sound.play()
        elif self.ball.sprite.x > x_max:
            self.ball.sprite.x = self.scene.width / 2 + 200
            self.ball.sprite.y = self.scene.height / 2
            self.ball.vx = -random.randint(300, 350)
            self.ball.vy = -random.randint(300, 350) * (-1 if random.randint(0, 1) == 0 else 1)
            self.scene.player_score += 1
            self.scene.player_label.text = str(self.scene.player_score)
            self.scene.point_sound.play()

        if (self.player.sprite.x < self.ball.sprite.x < self.player.sprite.x + self.scene.paddle_img.anchor_x and
                self.player.sprite.y - self.scene.paddle_img.anchor_y < self.ball.sprite.y < self.player.sprite.y + self.scene.paddle_img.anchor_y):
            self.ball.sprite.x = self.player.sprite.x + self.scene.paddle_img.anchor_x
            self.ball.vx *= -1
            self.scene.hit_sound.play()
        elif (self.cpu.sprite.x < self.ball.sprite.x < self.cpu.sprite.x + self.scene.paddle_img.anchor_x / 2 and
              self.cpu.sprite.y - self.scene.paddle_img.anchor_y < self.ball.sprite.y < self.cpu.sprite.y + self.scene.paddle_img.anchor_y):
            self.ball.sprite.x = self.cpu.sprite.x - self.scene.ball_img.anchor_x
            self.ball.vx *= -1
            self.scene.hit_sound.play()