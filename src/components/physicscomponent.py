from .component import Compoment_t

class PhysicsComponent_t(Compoment_t):
    def __init__(self, eID, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.entityID = eID

    def getEntityID(self):
        return self.entityID