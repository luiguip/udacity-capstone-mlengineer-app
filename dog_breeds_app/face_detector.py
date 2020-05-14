import cv2 

class FaceDetector:

    def __init__(self, image):
        self.image = image

    def face_detector(self) -> bool:
        number_faces : int = self.find_faces()
        if(self.has_more_than_one_face(number_faces)):
            raise ValueError("Image must have only one face!")
        elif(self.has_face(number_faces)):
            return True
        return False

    def find_faces(self) -> int:
        face_cascade = cv2.CascadeClassifier('dog_breeds_app/models/haarcascade_frontalface_alt.xml')
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        number_faces = len(faces)
        return number_faces

    def has_face(self, number_faces: int) -> bool:
        return number_faces > 0

    def has_more_than_one_face(self, number_faces: int) -> bool:
        return number_faces > 1

