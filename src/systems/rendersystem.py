import numpy as np
import cv2
from ..manager.entitymanager import EntityManager_t
from ..components.rendercomponent import  RenderComponent_t

class RenderSystem_t:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        window = np.zeros( (self.height, self.width, 3), dtype=np.uint8)
        window_name = "Game"
        cv2.namedWindow(window_name)

    def update(self, em: EntityManager_t):
        for ren in em.getRenderComponents():
            phy = ren.