from resourcemanager import ResourceManager


class PongResourceManager(ResourceManager):
    def __init__(self):
        super(PongResourceManager, self).__init__()
        self.paddle_img = self.load_image("paddle.png")
        self.ball_img = self.load_image("ball.png")
        self.hit_sound = self.load_sound("button-10.wav", streaming=False)
        self.point_sound = self.load_sound("point.wav", streaming=False)
