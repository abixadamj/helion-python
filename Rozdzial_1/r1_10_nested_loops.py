# program r1_10_nested_loops.py
# Przykłady dla zagnieżdżonych pętli for

test_object = ["Adam", "Beata", "Szymon", "Artur", "Magda"]
print(f"Testujemy dla obiektu: {test_object}")

for e in test_object:
    print(f"Sprawdzamy element: {e} ")
    licznik = 1
    for litera in e:
        if litera == "m":
            print(f"* Litera '{litera}' w imieniu {e} na pozycji {licznik}")
        licznik += 1

print("===[koniec]===")
