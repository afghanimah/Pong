import pyglet


def load_image(image_name):
    img = pyglet.resource.image(image_name)
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2
    return img


def load_sound(sound_name, streaming=True):
    return pyglet.resource.media(sound_name, streaming=streaming)
