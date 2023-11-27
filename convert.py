from pathlib import Path
import pytesseract
from PIL import Image
import sys

if len(sys.argv) != 3:
    sys.exit("Usage: python convert.py filename outputFilename")

image_file = sys.argv[1]
output = sys.argv[2] + ".txt"
out_directory = Path(r"~\Desktop").expanduser()
text_file = out_directory / Path(output)

with open(text_file, "a", encoding="utf-8") as output_file:
    pytesseract.pytesseract.tesseract_cmd = r" P A T H  T O  TESERECT.EXE " 
    text = str(pytesseract.image_to_string(Image.open(image_file)))
    text = text.replace("-\n", "")
    output_file.write(text)
