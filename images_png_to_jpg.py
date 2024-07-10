import os
from PIL import Image

# Path to the folder containing PNG images
png_folder = "D:/tobeconverted"

# Path to the folder where converted JPEG images will be saved
jpg_folder = "D:/jpgimages"

# Create the folder if it doesn't exist
os.makedirs(jpg_folder, exist_ok=True)

# Iterate over all files in the PNG folder
for filename in os.listdir(png_folder):
    # Check if the file is a PNG image
    if filename.endswith(".png"):
        # Open the PNG image
        png_image_path = os.path.join(png_folder, filename)
        with Image.open(png_image_path) as img:
            # Create the corresponding JPEG file path
            jpg_image_path = os.path.join(jpg_folder, filename.replace(".png", ".jpg"))
            # Convert and save the image as JPEG
            img.convert("RGB").save(jpg_image_path, "JPEG")

print("Conversion complete.")
