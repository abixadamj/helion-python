# program r1_13.py
# Przykłady dla wycinków (ang. slices)

napis = "To jest dosyć długi napis, który może mieć różną długość."

print(napis[:])  # Dokładna kopia
print(napis[::-1])  # Od końca do początku
print(napis[3:7])
print(napis[3:17])
print(napis[3:17:2])
print(napis[17:])
print(napis[-10::])  # Ostatnie 10 znaków
print(napis[:-10:-1])  # Ostatnie 10 znaków w odwróconej kolejności
print(napis[3:13])
# Poniżej wielokrotne odwołania - wycinki z wycinków
print(napis[3:13][:5])
print(napis[3:13][5:])
print(napis[3:13][5:][2:4])
