# program r7_00_walk.py
# Przykład użycia os.walk()

import os

directory = "."

for dirpath, dirname, files in os.walk(directory):
    print(f"dirpath = {dirpath}")
    print(f"dirname = {dirname}")
    print(f"files = {files}")
