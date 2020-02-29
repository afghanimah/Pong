from physicalentity import PhysicalEntity


class Paddle(PhysicalEntity):
    def __init__(self, img, x, y, speed, batch):
        super(Paddle, self).__init__(img, x, y, batch)
        self.speed = speed

    def follow(self, x, y):
        if self.sprite.y < y:
            self.vy = self.speed
        elif self.sprite.y > y:
            self.vy = -self.speed

    def update(self, dt):
        super(Paddle, self).update(dt)

    def draw(self):
        super(Paddle, self).draw()
