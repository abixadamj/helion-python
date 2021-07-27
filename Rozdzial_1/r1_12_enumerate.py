# program r1_12_enumerate.py
# Przykład dla pętli for - funkcja enumerate()

napis = "Python"
print(napis)
# Wykorzystujemy enumerate()
for nr, litera in enumerate(napis):
    print(f"Indeks: {nr} / wartość: {litera}")
