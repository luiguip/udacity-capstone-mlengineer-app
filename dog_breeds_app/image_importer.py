import cv2
from PIL import Image

class ImageImporter:

    def __init__(self, image_path: str):
        self.image_path = image_path

    def import_image_cv2(self):
        self.image_cv2 = cv2.imread(self.image_path)
        return self.image_cv2
    
    def import_image(self):
        self.image = Image.open(self.image_path)
        return self.image
