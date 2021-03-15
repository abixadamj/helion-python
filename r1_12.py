# program r1_12.py
# przykłady dla pętli for - funkcja range() , wycinki

napis = "Python i Linux"
dlugosc = len(napis)

print(f"Długość napisu '{napis}' to {dlugosc} znaków.")
print(f"Indeksy od 0 do {dlugosc-1}")

# co trzeci znak na ekran
for nr in range(0, dlugosc, 3):
    litera = napis[nr]
    print(f"Litera o indeksie {nr} to {litera}.")

# wycinki (ang. slices)
print("===============================")
print(f"Teraz wersja z wycinkami: {napis[::3]}")
