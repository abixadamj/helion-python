# program r7_01.py
# rozpoczynamy program

import os
from r7_functions import *


def exif_anonymize():

    directory = "."
    images_files = [".jpg", ".jpeg", ".png"]

    for dirpath, dirname, files in os.walk(directory):

        for file in files:
            image_file = os.path.join(dirpath, file)
            ext = os.path.splitext(image_file)[1].lower()
            print(f"Dla pliku: {image_file} rozszerzenie {ext}")

            if ext in images_files:
                print(f"Anonimizujemy plik: {image_file}")


if __name__ == "__main__":
    exif_anonymize()
else:
    print("Skrypt do wykonania samodzielnego.")
