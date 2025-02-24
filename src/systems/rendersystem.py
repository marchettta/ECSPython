import numpy as np
import cv2
from ..manager.entitymanager import EntityManager_t
from ..components.rendercomponent import  RenderComponent_t

class RenderSystem_t:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = np.zeros( (self.height, self.width, 3), dtype=np.uint8)
        self.window_name = 'Game'
        cv2.namedWindow(self.window_name)

    def clearScreen(self):
        self.window = np.zeros( (self.height, self.width, 3), dtype=np.uint8)

    def update(self, em: EntityManager_t):
        self.clearScreen()
        for ren in em.getRenderComponents():
            phy = em.getPhysicsComponentFromRenderComponent(ren)

            x = phy.x
            y = phy.y
            h = ren.height
            w = ren.width


            if x < 0 : x = 0
            if y < 0 : y = 0
            if x + ren.width  > self.width  : x = self.width - ren.width
            if y + ren.height > self.height : y = self.height - ren.height

            for c in range(3):
                self.window[y : y + h, x : x + w, c] = (
                ren.alpha * ren.png_image[: , :, c] + ( 1 - ren.alpha) * 
                self.window[y : y + h, x : x + w, c] )
            cv2.imshow(self.window_name, self.window)