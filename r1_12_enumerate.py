# program r1_12_enumerate.py
# przykłady dla pętli for - funkcja enumerate()

napis = "Python"
print(napis)
# wykorzystujemy enumerate()
for nr, litera in enumerate(napis):
    print(f"Indeks: {nr} / wartość: {litera}")
