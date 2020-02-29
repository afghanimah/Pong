from physicalentity import PhysicalEntity


class Ball(PhysicalEntity):
    def __init__(self, img, x, y, speed, batch):
        super().__init__(img, x, y, batch)
        self.speed = speed
