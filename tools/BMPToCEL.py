import subprocess
import os
import sys
from pathlib import Path

# Return a usage message if not enough arguments were supplied
if len(sys.argv) < 3:
    print("Usage: <input_directory> <working_directory>")
    exit()

input_directory = sys.argv[1]
working_directory = sys.argv[2]

CONVERSION_COMMAND = "tools\\BMPTo3DOCel.exe "

for bmp_path in Path(input_directory).rglob("*.bmp"):
    bmp_path = str(bmp_path)

    # Remove the initial "images" directory name from the path, then strip the .bmp ending
    output_cel = os.path.join(working_directory, bmp_path[bmp_path.index(os.path.sep) + 1:].replace(".bmp", ""))

    command = CONVERSION_COMMAND + bmp_path + " " + output_cel

    process_output = subprocess.run(command, stdout=subprocess.PIPE)

    # Since it doesn't report errors on stderr, scan and output any errors only
    for output_line in process_output.stdout.splitlines():
        output_line = output_line.decode("utf-8")
        if "must" in output_line:
            print("Error: " + bmp_path)
            print(output_line)
            print("\n")
