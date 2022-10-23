from pathlib import Path
import os
import sys
from PIL import Image

if len(sys.argv) < 3:
    print("Usage: <input_directory> <output_directory>")
    exit(1)

input_directory = sys.argv[1]
output_directory = sys.argv[2]

# Create the output path if it doesn't exist
Path(output_directory).mkdir(parents=True, exist_ok=True)


def swap_color(image, base_color, new_color):
    pixels = image.load()
    height, width = image.size

    for y in range(width):
        for x in range(height):
            if pixels[x, y] == base_color:
                pixels[x, y] = new_color

    return image


for path in Path(input_directory).rglob("*.png"):
    image = Image.open(path).convert("RGB")

    # Step 1: Change all the blue to black
    image = swap_color(image, (41, 131, 197), (0, 0, 0))

    # Step 2: Calculate the image size. Images must be multiples of 4 wide.
    new_width = image.getbbox()[2]
    if new_width % 4 != 0:
        new_width += 4 - new_width % 4

    image = image.crop((0, 0, new_width, 18))

    # Step 3: Convert the black to transparent
    image = swap_color(image, (0, 0, 0), (255, 0, 255))

    # Step 4: Save output file
    image.save(os.path.join(output_directory, path.name[:-4] + ".cel.bmp"), format="bmp")
