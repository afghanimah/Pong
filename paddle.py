from physicalentity import PhysicalEntity


class Paddle(PhysicalEntity):
    def __init__(self, img, x, y, speed, batch):
        super().__init__(img, x, y, batch)
        self.speed = speed

    def follow(self, _, y):
        if self.sprite.y < y:
            self.vy = self.speed
        elif self.sprite.y > y:
            self.vy = -self.speed
