from .component import Compoment_t
import cv2

class RenderComponent_t(Compoment_t):
    def __init__(self, eID, png_image_path):
        self.png_image = cv2.imread(png_image_path, cv2.IMREAD_UNCHANGED)
        if self.png_image is None:
            print("Error: Imagen no encontrada")
            exit()
        self.height, self.width = self.png_image.shape[:2]

        if self.png_image.shape[2] == 4:
            self.b, self.g, self.r, self.a = cv2.split(self.png_image)
            self.alpha = self.a / 255.0
        self.entityID = eID

    def getEntityID(self):
        return self.entityID