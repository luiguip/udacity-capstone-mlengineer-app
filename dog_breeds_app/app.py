from dog_breeds_app.dog_breed_detector import DogBreedDetector
from dog_breeds_app.face_detector import FaceDetector
from dog_breeds_app.image_importer import ImageImporter

def main(image_path: str, model_path="dog_breeds_app/models/model.pt", breeds_labels_path="dog_breeds_app/models/breeds_labels.p"):
    image_importer = ImageImporter(image_path)

    image_cv2 = image_importer.import_image_cv2()
    
    try:
        has_face = FaceDetector(image_cv2).face_detector()
    except ValueError:
        return "Invalid image. Have more than one person."

    image = image_importer.import_image()
    dog_breed_detect = DogBreedDetector(image, model_path, breeds_labels_path)

    dog_breed = dog_breed_detect.predict()

    a_or_an = "an" if dog_breed[0] in ['a', 'e', 'i', 'o', 'u'] else "a"
    
    if(has_face):
        output_str = "This person looks like {} {}"
    else:
        output_str =  "This dog is {} {}"

    return output_str.format(a_or_an, dog_breed)