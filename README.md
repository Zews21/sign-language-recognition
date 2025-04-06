# Sign Language Recognition with YOLOv8 🚀

## 📌 Project Overview
This project implements a **real-time sign language detector** using YOLOv8, trained on custom annotations from Label Studio to recognize 5 ASL signs.

## ✨ Key Features
- 📷 Real-time webcam detection (30+ FPS on GPU)
- 🏷️ Dataset labeled with [Label Studio](https://labelstud.io/) (YOLO format)
- 🏋️♂️ Custom-trained YOLOv8 model (94% mAP)

## 🛠️ Prerequisites
- Python 3.8+
- **Label Studio** (for annotation, [install instructions](#-label-studio-installation))
- **Hardware**:
  - NVIDIA GPU (recommended) + CUDA 11.8  
  *or*  
  - CPU-only mode (slower but works)

## 📦 Installation
```bash
# Clone repo
git clone https://github.com/Zews21/sign-language-recognition.git
cd sign-language-recognition

# Install dependencies
pip install -r requirements.txt
