"""
Inference engine and image pre-processing utilities.
"""

from typing import Dict, List, Tuple
from PIL import Image
import torch
import torch.nn.functional as F
from torchvision import transforms

from src.classes import CLASS_NAMES, DISEASE_INFO
from src.model import build_model


def get_inference_transforms():
    """
    Standard normalization for ImageNet-derived backbones.
    224x224 RGB image resized and scaled.
    """
    return transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])


class DiseasePredictor:
    """
    Lightweight, thread-safe predictor for plant disease classification.
    """
    def __init__(self, weights_path: str = None, device: str = None):
        if device is None:
            if torch.backends.mps.is_available():
                self.device = torch.device("mps")
            elif torch.cuda.is_available():
                self.device = torch.device("cuda")
            else:
                self.device = torch.device("cpu")
        else:
            self.device = torch.device(device)

        self.model = build_model(num_classes=len(CLASS_NAMES), pretrained=(weights_path is None))
        
        if weights_path:
            state_dict = torch.load(weights_path, map_location=self.device)
            self.model.load_state_dict(state_dict)
            
        self.model.to(self.device)
        self.model.eval()
        self.transform = get_inference_transforms()

    def predict(self, image: Image.Image, top_k: int = 3) -> Dict:
        """
        Classifies input PIL image and returns top predictions with advice.
        """
        if image.mode != "RGB":
            image = image.convert("RGB")

        tensor = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            outputs = self.model(tensor)
            probabilities = F.softmax(outputs, dim=1)[0]

        top_probs, top_indices = torch.topk(probabilities, top_k)
        
        top_predictions: List[Dict] = []
        for prob, idx in zip(top_probs, top_indices):
            class_name = CLASS_NAMES[idx.item()]
            info = DISEASE_INFO.get(class_name, {
                "crop": class_name.split("___")[0],
                "condition": class_name.split("___")[1] if "___" in class_name else class_name,
                "severity": "Unknown",
                "recommendation": "Consult a local agricultural extension specialist."
            })
            top_predictions.append({
                "class_name": class_name,
                "crop": info["crop"],
                "condition": info["condition"],
                "severity": info["severity"],
                "recommendation": info["recommendation"],
                "confidence": float(prob.item())
            })

        best = top_predictions[0]
        return {
            "predicted_class": best["class_name"],
            "crop": best["crop"],
            "condition": best["condition"],
            "severity": best["severity"],
            "recommendation": best["recommendation"],
            "confidence": best["confidence"],
            "top_k": top_predictions
        }
