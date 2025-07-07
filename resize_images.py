import os
from PIL import Image

# Configurable settings
input_folder = 'input_images'
output_folder = 'output_images'
new_size = (800, 600)  # Resize all images to this size

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            with Image.open(input_path) as img:
                resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                resized_img.save(output_path)
                print(f" Resized: {filename}")
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n All images processed!")
