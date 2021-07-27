# program test_wydajnosci.py
# Test wydajności Pythona w systemach Windows i Linux


# Wykorzystywane moduły
import sys

try:
    import matplotlib.pyplot as plt
except:
    if sys.platform == "linux":
        print("dla Linux (Debian/Ubuntu/Mint):")
        print("sudo apt install python3-pip")
        print("sudo -H pip3 install matplotlib")
    else:
        print("dla windows:")
        print("pip install matplotlib")
        print("pip install msvc-runtime")
    sys.exit(status=2)

# Reszta to standardowe moduły
import os
import pickle
import json
from random import random, randint, seed
from datetime import datetime
from math import sin, cos

# Funkcje pomocnicze
def zapis_danych(dane, nazwa_pliku="plik_danych.dat"):
    with open(nazwa_pliku, "wb") as p:
        pickle.dump(dane, p)


def odczyt_danych_testowych(plik="plik_danych.dat"):
    if not os.path.isfile(plik):
        return None

    with open(plik, "rb") as p:
        dane = pickle.load(p)
    return dane


def oblicz(lista, fun):
    from math import sin, cos

    out = []

    for x in lista:
        wart = eval(fun)
        out.append(wart)
    return out


def json_zapis(dane, nazwa_pliku="plik_danych.json"):
    with open(nazwa_pliku, "w") as outfile_e:
        json.dump(dane, outfile_e)


def zapis_wykresu(
    dane_x, dane_y, nazwa_pliku="wykres.png", nazwa_wykresu="Standardowy wykres xy"
):
    plt.figure(figsize=(40, 20), dpi=30)
    plt.scatter(dane_x, dane_y)
    plt.xlabel("dane_x")
    plt.ylabel("dane_y")
    plt.title(nazwa_pliku)
    plt.grid()
    plt.tight_layout()
    plt.savefig(nazwa_pliku)
    plt.close("all")


# Ustawienie stałego ziarna dla generatora liczb pseudolosowych tak, aby liczby zwracane przez
# generator były takie same przy kolejnych uruchomieniach testów.
seed(84376529347523)
start_time = datetime.now()

# Start - od tego momentu liczymy
wyniki = {
    "Aplikacja": "Program testowy",
    "Autor": "Adam Jurkiewicz",
    "sys.version": "",
    "sys.version_info": "",
    "os.uname": "",
    "Start": str(start_time),
    "Stop": None,
    "Delta_time": None,
    "Czasy co 1000 enumeracji": {},
}

wyniki[
    "sys.version"
] = f"{sys.version} | hexversion {sys.hexversion} | api {sys.api_version}"
wyniki["sys.version_info"] = str(sys.version_info)
if sys.platform == "linux":
    wyniki["os.uname"] = str(os.uname())

print("Start testu:")
for w in wyniki:
    print(f"{w}: {wyniki[w]}")
print("-----------------")
# 200 punktów podstawowych
dane_x = [x for x in range(-100, 100)]
zapis_danych(dane_x, "dane_wejsciowe.dat")


_1000 = 1
for i in range(1, 10000):
    # Odczyt danych podstawowych
    dane_x = odczyt_danych_testowych("dane_wejsciowe.dat")
    if i % 1000 == 0:
        time_now = datetime.now() - start_time
        wyniki["Czasy co 1000 enumeracji"][i] = str(time_now)
        print(f"Obliczam 1000: {i}")

    if i % 2 == 0:
        fun = str(f"sin({randint(1,10)}*x*x+{random()*i}*x-{i**randint(1,4)})")
        dane_y = oblicz(dane_x, fun)
    else:
        fun = str(f"cos({randint(1,i)}*x*x*(-1)+{randint(1,i)}*x+{i})")
        dane_y = oblicz(dane_x, fun)

    zapis_danych(dane_y, f"dane_wejsciowe{i}.dat")
    zapis_wykresu(dane_x, dane_y, f"wykres{i}.png")


stop_time = datetime.now()
wyniki["Stop"] = str(stop_time)
wyniki["Delta_time"] = str(stop_time - start_time)
json_zapis(wyniki)
