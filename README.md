# 🌿 Plant Disease Detection using Deep Learning

An optimized, lightweight Deep Learning project for crop leaf disease diagnosis and treatment recommendation built with **PyTorch**, **Torchvision**, and **Streamlit**.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.45+-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Overview

Early detection of agricultural plant diseases is vital to prevent crop loss and ensure food security. This project delivers an end-to-end, high-performance image classification pipeline designed to run efficiently on standard desktop CPUs or edge hardware without requiring bulky GPUs.

### Key Features
- **Lightweight Architecture**: Employs **MobileNetV3-Small** with transfer learning (~9.8 MB footprint), maximizing inference speed while preserving high diagnostic accuracy.
- **25+ Supported Plant Pathology Classes**: Covers key agricultural crops including **Apple**, **Corn (Maize)**, **Grape**, **Potato**, and **Tomato**.
- **Actionable Treatment Insights**: Outputs not just a disease label, but also severity categorization and targeted agricultural recommendations (e.g., biological controls, fungicide guidelines, cultural practices).
- **Interactive Web Interface**: Streamlit-powered GUI with drag-and-drop image upload, sample gallery, and top-3 prediction distribution charts.
- **End-to-End Workflow**: Includes training (`train.py`), inference (`inference.py`), model definitions (`model.py`), and web serving (`app.py`).

---

## 🗂️ Project Structure

```text
plant-disease-detection/
├── app.py                      # Interactive Streamlit Web Application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── models/                     # Saved model weights (.pth)
├── sample_images/              # Sample leaf photos for testing
│   ├── healthy_leaf.jpg
│   ├── diseased_leaf_spot.jpg
│   └── create_samples.py
└── src/
    ├── __init__.py
    ├── classes.py              # Crop categories and agronomic treatment guidance
    ├── model.py                # MobileNetV3 deep learning architecture
    ├── inference.py            # Prediction pipeline and preprocessing
    └── train.py                # Transfer learning training pipeline
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
Open your browser at `http://localhost:8501`.

---

## 🏋️‍♂️ Training on Custom Data

To train or fine-tune on your own dataset (e.g., the PlantVillage dataset):

1. Organize images in standard PyTorch ImageFolder layout:
```text
dataset/
├── train/
│   ├── Apple___Apple_scab/
│   └── Tomato___Early_blight/
└── val/
    ├── Apple___Apple_scab/
    └── Tomato___Early_blight/
```

2. Run the training script:
```bash
python3 src/train.py --data_dir dataset/ --epochs 10 --batch_size 32 --lr 0.001
```

The optimized weights will be saved to `models/plant_disease_model.pth`.

---

## 📊 Model Architecture & Efficiency

- **Backbone**: MobileNetV3-Small (pretrained on ImageNet)
- **Parameters**: ~1.5 Million (highly compact compared to ResNet-50's 25M)
- **Inference Latency**: ~15-25ms on CPU / Apple Silicon MPS
- **Image Input Resolution**: 224 × 224 pixels

---

## 👤 Author

- **Soham Deokar**
- GitHub: [@sohamdeokar101-coder](https://github.com/sohamdeokar101-coder)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
