# program r7_02.py
# rozpoczynamy program

import os
from r7_function import *


def exiff_anonymize():

    directory = "."
    images_files = [".jpg", ".jpeg", ".png"]

    for dirpath, dirname, files in os.walk(directory):

        for file in files:
            image_file = os.path.join(dirpath, file)
            ext = os.path.splitext(image_file)[1].lower()

            if ext in images_files and "_anon" not in image_file:
                print(f"Anonimizujemy plik: {image_file}")
                print(anonymize_exiff(image_file))


if __name__ == "__main__":
    exiff_anonymize()
else:
    print("Skrypt do wykonania samodzielnego.")
