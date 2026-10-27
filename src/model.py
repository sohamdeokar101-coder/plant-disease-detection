"""
Neural Network Architecture for Plant Disease Classification.
Uses an optimized MobileNetV3-Small backbone with a custom classifier head.
Designed for high throughput, low CPU/RAM footprint, and real-time edge/desktop inference.
"""

import torch
import torch.nn as nn
from torchvision import models


def build_model(num_classes: int = 25, pretrained: bool = True) -> nn.Module:
    """
    Builds a MobileNetV3-Small architecture customized for leaf disease diagnosis.
    
    Args:
        num_classes (int): Number of target disease & healthy classes.
        pretrained (bool): Load ImageNet pre-trained weights for transfer learning.
    
    Returns:
        nn.Module: Configured PyTorch model ready for training or evaluation.
    """
    weights = models.MobileNet_V3_Small_Weights.DEFAULT if pretrained else None
    model = models.mobilenet_v3_small(weights=weights)

    # In mobilenet_v3_small, classifier is a Sequential:
    # (0): Linear(in_features=576, out_features=1024)
    # (1): Hardswish()
    # (2): Dropout(p=0.2)
    # (3): Linear(in_features=1024, out_features=1000)
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Sequential(
        nn.Linear(in_features, num_classes)
    )

    return model


if __name__ == "__main__":
    net = build_model(num_classes=25, pretrained=False)
    dummy_input = torch.randn(1, 3, 224, 224)
    out = net(dummy_input)
    print(f"Model instantiated successfully! Output tensor shape: {out.shape}")
