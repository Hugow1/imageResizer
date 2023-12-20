import os
import sys
from PIL import Image

def resize_image(input_path, output_path, max_width):
    with Image.open(input_path) as img:
        width, height = img.size

        # Resize only if the image is wider than the specified max width
        if width > max_width:
            new_height = int(max_width * height / width)
            resized_img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            resized_img.save(output_path)
            print(f"Resized {input_path} and saved to {output_path}")

def main(folder_path, max_width):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(folder_path, filename)
            output_path = input_path  # Change this if you want to save as a new file
            resize_image(input_path, output_path, max_width)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <folder_path> <max_width>")
        sys.exit(1)

    folder_path = sys.argv[1]
    max_width = int(sys.argv[2])

    main(folder_path, max_width)
