import cv2
from ..manager.entitymanager import EntityManager_t

class InputSystem_t:
    def __init__(self):
        pass

    def update(self, em: EntityManager_t):
        self.key = cv2.pollKey()
        global game_over
        for inp in em.getInputComponents():
            phy = em.getPhysicsComponentFromInputComponent(inp)
            if self.key == inp.key_LEFT: phy.x -= 1
            if self.key == inp.key_RIGHT: phy.x += 1
            if self.key == inp.key_UP: phy.y -= 1
            if self.key == inp.key_DOWN:phy.y += 1
            if self.key == ord('q'):
                game_over = 1