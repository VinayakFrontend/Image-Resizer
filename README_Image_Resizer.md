
# 🖼️ Image Resizer Tool (Batch)

A simple Python tool to **resize multiple images in batch** using the Pillow library.

---

## ✅ Features

- Resize all images in a folder to a specified size
- Supports common image formats (`.jpg`, `.png`, `.jpeg`, `.bmp`, `.gif`)
- Automatically creates output folder
- Easy to customize (size, folder path, etc.)

---

## 🛠️ Tools Used

- Python 🐍
- Pillow (`PIL`)
- `os` module

---

## 📁 Folder Structure

```
image_resizer/
├── input_images/        # Place original images here
├── output_images/       # Resized images will be saved here
└── resize_images.py     # Main script
```

---

## 📜 How to Use

1. Install Pillow if not already:
    ```bash
    pip install pillow
    ```

2. Put your images inside the `input_images/` folder.

3. Run the script:
    ```bash
    python resize_images.py
    ```

4. Resized images will be saved in `output_images/` folder.

---

## ✏️ Sample Code Snippet

```python
from PIL import Image
import os

input_folder = 'input_images'
output_folder = 'output_images'
new_size = (800, 600)

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
            resized_img.save(output_path)
```

---


