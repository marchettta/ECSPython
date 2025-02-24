from .component import Compoment_t

class InputComponent_t(Compoment_t):
    def __init__(self, eID):
        self.key_LEFT = 2424832
        self.key_UP = 2490368
        self.key_DOWN = 2621440
        self.key_RIGTH = 2555904
        self.entityID = eID

    def getEntityID(self):
        return self.entityID