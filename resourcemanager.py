import pyglet


class ResourceManager:
    def __init__(self):
        self.paddle_img = self.load_image("paddle.png")
        self.ball_img = self.load_image("ball.png")
        self.hit_sound = self.load_sound("button-10.wav", streaming=False)
        self.point_sound = self.load_sound("point.wav", streaming=False)

    @staticmethod
    def load_image(image_name, center=True):
        # resource.image loads into textureatlas by default
        img = pyglet.resource.image(image_name)
        if center:
            img.anchor_x = img.width // 2
            img.anchor_y = img.height // 2
        return img

    @staticmethod
    def load_sound(sound_name, streaming=True):
        return pyglet.resource.media(sound_name, streaming=streaming)
