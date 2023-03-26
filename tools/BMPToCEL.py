import subprocess
import os
import sys
import shutil
from pathlib import Path

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <input_directory> <working_directory>")
    exit()

input_directory = sys.argv[1]
working_directory = sys.argv[2]

CONVERSION_COMMAND = "tools\\3it_win64.exe to-cel --transparent magenta "

for bmp_path in Path(input_directory).rglob("*.bmp"):
    bmp_path = str(bmp_path)

    # Remove the initial "images" directory name from the path, then strip the .bmp ending
    tool_output = bmp_path + "_uncoded_unpacked_16bpp.cel"
    output_cel = os.path.join(working_directory, bmp_path[bmp_path.index(os.path.sep) + 1:]).replace(".bmp", "")

    command = CONVERSION_COMMAND + bmp_path

    process_output = subprocess.run(command, stdout=subprocess.PIPE)

    # Move the file to the right spot
    shutil.move(tool_output, output_cel)

    # Since it doesn't report errors on stderr, scan and output any errors only
    # Note: this was for the old tool, so probably isn't that useful, but left around to see how it worked
    for output_line in process_output.stdout.splitlines():
        output_line = output_line.decode("utf-8")
        if "must" in output_line or "BMP is not" in output_line:
            print("Error: " + bmp_path)
            print(output_line)
            print("\n")
