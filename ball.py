from physicalentity import PhysicalEntity


class Ball(PhysicalEntity):
    def __init__(self, img, x, y, speed, batch):
        super(Ball, self).__init__(img, x, y, batch)
        self.speed = speed

    def update(self, dt):
        super(Ball, self).update(dt)

    def draw(self):
        super(Ball, self).draw()
