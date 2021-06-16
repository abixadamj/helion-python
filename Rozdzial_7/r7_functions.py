# program r7_functions.py
# funkcje dodatkowe

import sys
import os
from exif import Image


def test_file(file: str) -> bool:
    """Sprawdzamy istnienie pliku"""
    if not os.path.exists(file):
        return False
    return True


def open_image(file: str) -> Image:
    """Otwieramy plik graficzny
    r = Read-Only (tylko do odczytu)
    b = Binary (tryb binarny dostępu do pliku)"""
    with open(file, "rb") as image_file:
        try:
            image = Image(image_file)
        except:
            return False
    # po zamknięciu pliku
    return image


def info_exif(file_name: str):
    """Pobieramy dane Exiff i wyświetlamy je"""
    if not test_file(file_name):
        print(f"Brak pliku: {file_name}")
        return None

    image_data = open_image(file_name)
    if not image_data:
        print("Błędne dane")
        return None

    if not image_data.has_exif:
        print(f"Brak danych EXIFF dla : {file_name}")
        return None

    image_attribs = image_data.get_all()
    for attrib in image_attribs:
        value = image_attribs[attrib]
        print(f"Atrybut: {attrib} = {value}")


def anonymize_exif(file_name: str) -> str:
    """Zastępujemy oryginalne dane Exiff naszymi wymyślonymi"""

    image_data = open_image(file_name)
    if not image_data:
        return "Błędne dane"

    if not image_data.has_exif:
        return f"Brak danych EXIFF dla : {file_name}"

    image_attribs = image_data.get_all()
    for attrib in image_attribs:
        if "gps" in attrib or "maker_note" in attrib or "date" in attrib:
            del image_data[attrib]
        elif "make" in attrib or "model" in attrib or "software" in attrib:
            image_data[attrib] = "Python"

    new_file = os.path.splitext(file_name)[0] + "_anon" + os.path.splitext(file_name)[1]

    with open(new_file, "wb") as anon_file:
        anon_file.write(image_data.get_file())

    return f"OK -> {new_file}"


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        print(f"Uruchamiamy dla jednego pliku: {args[1]} - informacje:")
        info_exif((args[1]))
        sys.exit(0)
    else:
        print(f"Wywołanie samego skryptu {args[0]} niemożliwe.")
        sys.exit(2)
