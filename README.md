# 🌿 Plant Disease Detection using Deep Learning

An optimized, lightweight Deep Learning project for crop leaf disease diagnosis and treatment recommendations built with **PyTorch**, **Torchvision**, **Streamlit**, and the **PlantVillage Kaggle Dataset**.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B.svg)](https://streamlit.io/)
[![Kaggle Dataset](https://img.shields.io/badge/Dataset-PlantVillage-20BEFF.svg)](https://www.kaggle.com/datasets/emmarex/plantdisease)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

Early detection of agricultural plant diseases is vital to prevent crop loss and ensure food security. This project provides an end-to-end image classification pipeline trained and evaluated on real-world crop leaf pathology images from the **Kaggle PlantVillage Dataset**.

Designed for high efficiency, it runs smoothly on standard desktop CPUs and Apple Silicon without requiring heavy enterprise GPUs.

### Key Features
- **Authentic Dataset**: Uses real leaf photos from the benchmark **PlantVillage Kaggle Dataset** covering healthy leaves and various bacterial, fungal, and viral infections.
- **Lightweight Architecture**: Employs **MobileNetV3-Small** with transfer learning (~9.8 MB footprint), offering lightning-fast inference (<25ms).
- **25+ Supported Plant Pathology Classes**: Covers key agricultural crops including **Apple**, **Corn (Maize)**, **Grape**, **Potato**, and **Tomato**.
- **Actionable Treatment Insights**: Outputs not just a disease label, but also severity categorization and targeted agricultural recommendations (e.g., biological controls, fungicide guidelines, cultural practices).
- **Interactive Web Interface**: Streamlit-powered GUI with drag-and-drop image upload, real sample test gallery, and top-3 prediction distribution charts.
- **Automated Kaggle Integration**: Includes a built-in script (`src/download_kaggle_dataset.py`) to fetch and extract the dataset via the Kaggle API.

---

## 🗂️ Project Structure

```text
plant-disease-detection/
├── app.py                      # Interactive Streamlit Web Application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules (excludes bulky data/checkpoints)
├── README.md                   # Project documentation
├── models/                     # Saved model checkpoints (.pth)
├── sample_images/              # Authentic leaf samples from PlantVillage
│   ├── real_apple_healthy.jpg
│   ├── real_apple_scab.jpg
│   ├── real_corn_common_rust.jpg
│   ├── real_grape_black_rot.jpg
│   ├── real_potato_early_blight.jpg
│   ├── real_tomato_early_blight.jpg
│   ├── real_tomato_healthy.jpg
│   └── real_tomato_late_blight.jpg
└── src/
    ├── __init__.py
    ├── classes.py              # Crop categories and agronomic treatment guidance
    ├── model.py                # MobileNetV3 deep learning architecture
    ├── inference.py            # Prediction pipeline and preprocessing
    ├── train.py                # Transfer learning training pipeline
    └── download_kaggle_dataset.py # Automated Kaggle dataset downloader
```

---

## 🛠️ Supported Crops & Pathologies

| Crop | Conditions Detected |
| :--- | :--- |
| **Apple** | Apple Scab, Black Rot, Cedar Apple Rust, Healthy |
| **Corn (Maize)** | Cercospora Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| **Grape** | Black Rot, Esca (Black Measles), Leaf Blight, Healthy |
| **Potato** | Early Blight, Late Blight, Healthy |
| **Tomato** | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/sohamdeokar101-coder/plant-disease-detection.git
cd plant-disease-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501` to test with uploaded images or the included genuine PlantVillage sample gallery.

---

## 📦 Fetching the Kaggle Dataset

### Option 1: Automated Download via Kaggle CLI
Ensure your `kaggle.json` API token is in `~/.kaggle/`:
```bash
python3 src/download_kaggle_dataset.py --output_dir dataset/
```

### Option 2: Manual Download
Download the dataset directly from Kaggle:
- [Kaggle PlantVillage Dataset by emmarex](https://www.kaggle.com/datasets/emmarex/plantdisease) or
- [New Plant Diseases Dataset by vipoooool](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)

Extract the dataset so the directory contains `train/` and `val/` subfolders:
```text
dataset/
├── train/
│   ├── Apple___Apple_scab/
│   └── Tomato___Early_blight/
└── val/
    ├── Apple___Apple_scab/
    └── Tomato___Early_blight/
```

---

## 🏋️‍♂️ Model Training

To train or fine-tune on the downloaded Kaggle dataset:
```bash
python3 src/train.py --data_dir dataset/ --epochs 10 --batch_size 32 --lr 0.001
```

The optimized model weights will be saved to `models/plant_disease_model.pth`.

---

## 📊 Model Architecture & Efficiency

- **Backbone**: MobileNetV3-Small (pretrained on ImageNet)
- **Parameters**: ~1.5 Million (ultra-compact compared to ResNet-50's 25M)
- **Inference Latency**: ~15-25ms on CPU / Apple Silicon MPS
- **Image Input Resolution**: 224 × 224 pixels

---

## 👤 Author

- **Soham Deokar**
- GitHub: [@sohamdeokar101-coder](https://github.com/sohamdeokar101-coder)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
