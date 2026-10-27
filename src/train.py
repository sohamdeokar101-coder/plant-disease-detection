"""
Lightweight training pipeline with PyTorch and torchvision.
Supports dataset directory structure formatted in standard ImageFolder:
    dataset_root/
        train/
            class_name_1/
            class_name_2/
        val/
            class_name_1/
            class_name_2/
"""

import argparse
import os
import time
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from src.classes import CLASS_NAMES
from src.model import build_model


def get_data_loaders(data_dir: str, batch_size: int = 32, num_workers: int = 2):
    train_transform = transforms.Compose([
        transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    val_transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    train_path = os.path.join(data_dir, "train")
    val_path = os.path.join(data_dir, "val")

    if not os.path.exists(train_path):
        raise FileNotFoundError(f"Missing training directory: {train_path}")

    train_dataset = datasets.ImageFolder(train_path, transform=train_transform)
    val_dataset = datasets.ImageFolder(val_path, transform=val_transform) if os.path.exists(val_path) else None

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=num_workers) if val_dataset else None

    return train_loader, val_loader, train_dataset.classes


def train(data_dir: str, epochs: int = 5, batch_size: int = 32, lr: float = 1e-3, output_model: str = "models/plant_disease_model.pth"):
    device = torch.device("mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu")
    print(f"Training on device: {device}")

    train_loader, val_loader, detected_classes = get_data_loaders(data_dir, batch_size=batch_size)
    num_classes = len(detected_classes)
    print(f"Detected {num_classes} classes from dataset.")

    model = build_model(num_classes=num_classes, pretrained=True)
    model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    best_acc = 0.0
    os.makedirs(os.path.dirname(output_model), exist_ok=True)

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        start_time = time.time()

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

        scheduler.step()
        train_acc = (correct / total) * 100 if total > 0 else 0
        epoch_loss = running_loss / total if total > 0 else 0

        val_acc = 0.0
        if val_loader:
            model.eval()
            val_correct = 0
            val_total = 0
            with torch.no_grad():
                for images, labels in val_loader:
                    images, labels = images.to(device), labels.to(device)
                    outputs = model(images)
                    _, preds = torch.max(outputs, 1)
                    val_correct += (preds == labels).sum().item()
                    val_total += labels.size(0)
            val_acc = (val_correct / val_total) * 100 if val_total > 0 else 0

        elapsed = time.time() - start_time
        print(f"Epoch [{epoch+1}/{epochs}] ({elapsed:.1f}s) - Loss: {epoch_loss:.4f} - Train Acc: {train_acc:.2f}%" + (f" - Val Acc: {val_acc:.2f}%" if val_loader else ""))

        target_acc = val_acc if val_loader else train_acc
        if target_acc >= best_acc:
            best_acc = target_acc
            torch.save(model.state_dict(), output_model)
            print(f"--> Saved best model weights to {output_model}")

    print("Training complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train lightweight plant disease classifier")
    parser.add_argument("--data_dir", type=str, required=True, help="Path to dataset root containing train/ and optional val/")
    parser.add_argument("--epochs", type=int, default=5, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size")
    parser.add_argument("--lr", type=float, default=1e-3, help="Learning rate")
    parser.add_argument("--output", type=str, default="models/plant_disease_model.pth", help="Target model file path")
    args = parser.parse_args()

    train(args.data_dir, epochs=args.epochs, batch_size=args.batch_size, lr=args.lr, output_model=args.output)
