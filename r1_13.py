# program r1_13.py
# przykłady dla wycinków (ang. slices)

napis = "To jest dosyć długi napis, który może mieć różną wielkość."

print(napis[:])  # dokładna kopia
print(napis[::-1])  # od końca do początku
print(napis[3:7])
print(napis[3:17])
print(napis[3:17:2])
print(napis[17:])
print(napis[-10::])  # ostatnie 10 znaków
print(napis[:-10:-1])  # ostatnie 10 znaków w odwróconej kolejności
print(napis[3:13])
# poniżej wielokrotne odwołania wycinków z wycinków
print(napis[3:13][:5])
print(napis[3:13][5:])
print(napis[3:13][5:][2:4])
