import sys
from PIL import Image

if len(sys.argv) < 2:
    print("Usage: <input_image>")

image = Image.open(sys.argv[1])


def swap_color(image, base_color, new_color):
    pixels = image.load()
    height, width = image.size

    for y in range(width):
        for x in range(height):
            if pixels[x, y] == base_color:
                pixels[x, y] = new_color

    return image


image = swap_color(image, (0, 0, 0), (255, 0, 255))
image.save(sys.argv[1])
