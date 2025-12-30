# 🔤 Tifinagh Mini Project - OCR System

> **Computer Vision Project**: Optical Character Recognition (OCR) for Tifinagh Script

A Python-based OCR (Optical Character Recognition) system designed to automatically segment and extract Tifinagh characters from scanned images. This project uses OpenCV for image processing and character extraction.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Output](#output)
- [Contributing](#contributing)

---

## 🎯 Overview

This project implements an automated segmentation system for **Tifinagh characters** (ⵜⵉⴼⵉⵏⴰⵖ), the writing system used for Berber languages. The system processes scanned images containing handwritten Tifinagh letters and automatically extracts individual characters for dataset creation.

**Key Objective**: Create a structured dataset of Tifinagh characters from scanned images to enable future machine learning and recognition tasks.

---

## ✨ Features

- ✅ **Automated Character Segmentation**: Automatically detects and extracts individual characters from scanned images
- ✅ **Binary Image Processing**: Converts scanned images to binary (black & white) for optimal character extraction
- ✅ **Noise Filtering**: Removes small artifacts and noise from the scanned images
- ✅ **Batch Processing**: Processes multiple images (1-33) in a single run
- ✅ **Organized Output**: Creates a structured dataset with separate folders for each letter class
- ✅ **Configurable Parameters**: Easy-to-adjust thresholds and filters for different image qualities

---

## 📁 Project Structure

```
tifinagh_mini_project/
├── scans/                    # Input folder containing scanned images (1.jpeg to 33.jpeg)
├── dataset/                  # Output folder with extracted characters
│   ├── 1/                   # Extracted samples for letter 1
│   ├── 2/                   # Extracted samples for letter 2
│   └── ...                  # ... up to 33
├── segmentation_auto.py     # Main segmentation script
└── README.md               # Project documentation
```

---

## 🔧 Requirements

- Python 3.7+
- OpenCV (cv2)
- NumPy (installed automatically with opencv-python)

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/SatushiNakamot0/tifinagh_mini_project.git
cd tifinagh_mini_project
```

### 2. Install Dependencies

```bash
pip install opencv-python
```

Or install all dependencies from requirements file (if available):

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Step 1: Prepare Your Images

Place your scanned Tifinagh letter images in the `scans/` folder. Images should be named numerically:
- `1.jpeg` (or `1.jpg`)
- `2.jpeg` (or `2.jpg`)
- ... up to `33.jpeg` (or `33.jpg`)

### Step 2: Run the Segmentation Script

```bash
python segmentation_auto.py
```

### Step 3: Check the Output

The extracted characters will be saved in the `dataset/` folder, organized by letter class.

---

## ⚙️ How It Works

The segmentation process follows these steps:

### 1. **Image Loading**
   - Loads each scanned image from the `scans/` folder
   - Converts the image to grayscale

### 2. **Image Binarization**
   - Applies **THRESH_BINARY_INV** + **OTSU** threshold
   - Converts white background (paper) → black (0)
   - Converts black ink (letters) → white (255)

### 3. **Contour Detection**
   - Finds external contours in the binary image
   - Each contour represents a potential character

### 4. **Filtering & Extraction**
   - Filters out small noise (width > 20px and height > 20px)
   - Adds a 5px margin around each character
   - Extracts the Region of Interest (ROI)

### 5. **Saving**
   - Saves each extracted character as a PNG file
   - Organizes by class in separate folders

### Technical Parameters:

```python
SOURCE_DIR = "scans"     # Input folder
OUTPUT_DIR = "dataset"   # Output folder
MIN_WIDTH = 20          # Minimum character width
MIN_HEIGHT = 20         # Minimum character height
MARGIN = 5              # Margin around character
```

---

## 📊 Output

After running the script, you'll get:

```
dataset/
├── 1/
│   ├── 0.png
│   ├── 1.png
│   └── ...
├── 2/
│   ├── 0.png
│   └── ...
└── 33/
    ├── 0.png
    └── ...
```

Each PNG file contains a **white character on a black background**, ready for machine learning training or further processing.

### Sample Output Messages:

```
Traitement de la lettre 1...
   -> 0 exemples tkharja (fond ka7al).
Traitement de la lettre 2...
   -> 1 exemples tkharja (fond ka7al).
...
Extraction salat ! chof l folder 'dataset'.
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some improvement'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Open a Pull Request

---

## 📝 Notes

- **Image Quality**: For best results, use high-quality scans with good contrast
- **Character Size**: Adjust `MIN_WIDTH` and `MIN_HEIGHT` if characters are too small or too large
- **File Format**: The script supports both `.jpeg` and `.jpg` formats
- **Empty Results**: If some letters show 0 extracted examples, they might be too small or have poor contrast

---

## 📧 Contact

**Yazid Tahiri Alaoui**  
GitHub: [@SatushiNakamot0](https://github.com/SatushiNakamot0)

---

## 📄 License

This project is open source and available for educational purposes.

---

