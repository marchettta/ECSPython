import numpy as np
import cv2
from ..manager.entitymanager import EntityManager_t
from ..components.rendercomponent import  RenderComponent_t

class RenderSystem_t:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = np.zeros( (self.height, self.width, 3), dtype=np.uint8)
        self.window_name = "Game"
        cv2.namedWindow(self.window_name)

    def update(self, em: EntityManager_t):
        for ren in em.getRenderComponents():
            phy = em.getPhysicsComponentFromRenderComponent(ren)
            for c in range(3):
                self.window[phy.y : phy.y + ren.height, phy.x : phy.x + ren.width, c] = (
                ren.alpha * ren.png_image[: , :, c] + ( 1 - ren.alpha) * 
                self.window[phy.y : phy.y + ren.height, phy.x : phy.x + ren.width, c] )
                cv2.imshow(self.window_name, self.window)