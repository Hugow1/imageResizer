# Image Resizer

## Overview
The Image Resizer is a Python script that allows users to batch resize images in a specified folder. It's designed to scale down images that exceed a given maximum width, maintaining their aspect ratios.

## Features
- Batch processes all JPEG and PNG files in a specified directory.
- Resizes images that are wider than the specified maximum width.
- Maintains the aspect ratio of each image.
- Overwrites the original files with the resized versions (or can be modified to save new copies).

## Requirements
- Python 3
- Pillow library

## Installation
1. **Install Python 3:** Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Pillow:** Pillow is a fork of PIL (Python Imaging Library) and is required for image processing. Install it using pip:
   ```bash
   pip3 install Pillow

## Usage
1. **Place the Script:** Download resizeImages.py and place it in a directory of your choice.

2. **Run the Script:** Open a terminal and navigate to the directory where the script is located. Run the script using the following command:
  ```bash
  python3 resizeImages.py <path_to_image_folder> <max_width>
  ```
  **<path_to_image_folder>:** The path to the folder containing the images you want to resize.
  **<max_width>:** The maximum width (in pixels) for the images. Images wider than this will be resized.
