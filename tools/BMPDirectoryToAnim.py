import subprocess
import os
import sys
import glob
from pathlib import Path
from PIL import Image

if len(sys.argv) < 4:
    print("Usage: <base_input_dir> <base_preprocess_dir> <base_output_directory>")

input_directory = Path(sys.argv[1])
preprocess_directory = Path(sys.argv[2])
output_directory = Path(sys.argv[3])

CONVERSION_COMMAND = "tools\\BMPTo3DOAnim.exe"


def swap_color(image, base_color, new_color):
    pixels = image.load()
    height, width = image.size

    for y in range(width):
        for x in range(height):
            if pixels[x, y] == base_color:
                pixels[x, y] = new_color

    return image


# Create the output directory just in case
preprocess_directory.mkdir(parents=True, exist_ok=True)

anim_folders = set()

# Step 1: Scan the anim directory and find all folders that contain bmps
for bmp_path in input_directory.rglob("*.bmp"):
    anim_folders.add(bmp_path.parent)

for anim_folder in anim_folders:
    # Step 2: Make a sprite sheet based off the images in the folder
    print(f"Processing: {anim_folder}")
    frames = glob.glob(os.path.join(str(anim_folder), "*.bmp"))
    frame_count = len(frames)

    # Determine the size of the sprite sheet using the frame count and the first image dimensions
    first_frame = Image.open(frames[0])
    width, height = first_frame.size
    canvas = Image.new("RGB", (width * frame_count, height))

    # Add each frame to the sprite sheet
    for index, frame in enumerate(frames):
        frame_image = Image.open(frame)
        canvas.paste(frame_image, (width * index, 0))

    # Make all pure black colors transparent
    canvas = swap_color(canvas, (0, 0, 0), (255, 0, 255))

    # Save off the sprite sheet in the output directory while maintaining the directory structure
    input_relative = anim_folder.relative_to(input_directory)
    sprite_sheet_path = preprocess_directory.joinpath(input_relative)
    output_path = output_directory.joinpath(input_relative)
    sprite_sheet_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(str(sprite_sheet_path) + ".bmp", "BMP")

    # Step 3: Turn it into an anim file
    command = f"{CONVERSION_COMMAND} {width} {height} {str(sprite_sheet_path)}.bmp {str(output_path)}.ANIM"
    process_output = subprocess.run(command, stdout=subprocess.PIPE)

    for output_line in process_output.stdout.splitlines():
        output_line = output_line.decode("utf-8")
        if "must" in output_line or "BMP is not" in output_line:
            print("Error: " + anim_folder.name)
            print(output_line)
            print("\n")

    print(f"Finished {anim_folder.name}!\n")
