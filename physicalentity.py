from entity import Entity


class PhysicalEntity(Entity):
    def __init__(self, img, x, y, batch):
        super().__init__(img, x, y, batch)
        self.vx = 0
        self.vy = 0

    def update(self, dt):
        super().update(dt)
        self.sprite.x += self.vx * dt
        self.sprite.y += self.vy * dt
