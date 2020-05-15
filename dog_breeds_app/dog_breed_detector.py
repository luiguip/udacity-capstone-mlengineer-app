import torch
import torch.nn as nn
import torchvision.models as models
import torchvision.transforms as transforms
import pickle

class DogBreedDetector:

    def __init__(self, image, model_path, breeds_labels_path):
        self.image = image
        self.model = self.import_model(model_path)
        self.breeds_labels = self.import_breeds_labels(breeds_labels_path)
    
    def import_model(self, model_path):
        model = models.vgg16()
        n_inputs = model.classifier[6].in_features
        last_layer = nn.Linear(n_inputs, 133)
        model.classifier[6] = last_layer
        raw_model = torch.load(model_path, map_location='cpu')
        model.load_state_dict(raw_model)
        model.eval()
        return model

    def import_breeds_labels(self, breeds_labels_path):
        breeds_labels = pickle.load(open(breeds_labels_path, "rb"))
        return breeds_labels
    
    def predict(self):
        transform_pipeline = self.create_transform_pipeline()
        img_t = transform_pipeline(self.image)
        batch_t = torch.unsqueeze(img_t, 0)
        out = self.model(batch_t)
        out_cpu = out
        _, index_tensor = torch.max(out_cpu, 1)
        index = index_tensor.numpy()[0]
        return self.breeds_labels[index]
    
    def create_transform_pipeline(self):
        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                    std=[0.229, 0.224, 0.225])
        
        transform_pipeline = transforms.Compose([
                                                transforms.Resize(256),        
                                                transforms.CenterCrop(224),
                                                transforms.ToTensor(),
                                                normalize
                                                ])
        return transform_pipeline