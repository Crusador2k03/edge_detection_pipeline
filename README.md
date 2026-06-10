# Edge Detection on Industrial Images

## Overview

This project implements a classical computer vision pipeline for edge extraction from industrial images using OpenCV. The objective is to identify structural boundaries and geometric features in industrial components such as gears, circuit boards, and machine parts.

The pipeline applies image preprocessing techniques followed by Canny edge detection to generate clean and informative edge maps suitable for inspection, feature extraction, and downstream computer vision tasks.

---

## Features

- Image loading and preprocessing
- Grayscale conversion
- Gaussian noise reduction
- Canny edge detection
- Comparative analysis on noisy images
- Batch processing of multiple industrial images
- Automated output image generation

---

## Methodology

The processing pipeline follows the sequence:

```text
Input Image
     ↓
Grayscale Conversion
     ↓
Gaussian Blur
     ↓
Canny Edge Detection
     ↓
Edge Map Generation
```

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Results

The pipeline successfully extracts edges from:
- Gears
- Circuit Boards
- Machine Parts
- Metal Components

## Installation

requirements.txt is a list of all dependencies required to run the pipeline on your system.
- Run the below command in your terminal:

```bash
pip install -r requirements.txt
```

## Running the program
Run this on your terminal to start using the pipeline:
```bash
python edge_detection.py
```

## Results

### Gear

![Gear Result](outputs\gear_20260610_234211.png)

### Circuit Board

![Circuit Result](outputs\circuit_board_20260610_234032.png)

### Machine Parts

![Machine Parts Result](outputs\machine_parts_20260610_234133.png)
