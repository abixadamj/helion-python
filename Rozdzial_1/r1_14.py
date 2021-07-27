# program r1_14.py
# Przykłady dla enumerate()

napis = "To jest napis."
for nr, wartosc in enumerate(napis):
    print(f"Element o indeksie {nr} ma wartość {wartosc}")

print("===================================")
test_object = [3, -4, 2, 4.5, 1]
for nr, wartosc in enumerate(test_object):
    print(f"Element o indeksie {nr} ma wartość {wartosc}")

print("===================================")
test_object = (3, [-4, 2], 4.5, 1)
for nr, wartosc in enumerate(test_object):
    print(f"Element o indeksie {nr} ma wartość {wartosc}")
    if type(wartosc) is list:
        print("Ten element to lista.")
