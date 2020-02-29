import pyglet


class ResourceManager:
    reindex_done = False

    def __init__(self):
        self.resources = {}

    @staticmethod
    def reindex():
        if ResourceManager.reindex_done:
            return
        ResourceManager.reindex_done = True
        pyglet.resource.path = ['resources/']
        pyglet.resource.reindex()

    def load_image(self, image_name, ext="png", center=True):
        # resource.image loads into texture atlas by default
        ResourceManager.reindex()

        img = self.resources.get(image_name)
        if img is not None:
            return img

        img = pyglet.resource.image(image_name + "." + ext)
        if center:
            img.anchor_x = img.width // 2
            img.anchor_y = img.height // 2
        self.resources[image_name] = img

        return img

    def load_sound(self, sound_name, ext="wav", streaming=False):
        ResourceManager.reindex()

        sound = self.resources.get(sound_name)
        if sound is not None:
            return sound

        sound = pyglet.resource.media(sound_name + "." + ext, streaming=streaming)
        self.resources[sound_name] = sound

        return sound
