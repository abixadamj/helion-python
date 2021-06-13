# program r1_10_continue.py
# przykłady dla pętli for i continue

test_object = ["Adam", "Beata", "Szymon", "Artur", "Magda"]
print(f"Testujemy dla obiektu: {test_object}")

for e in test_object:
    if e[0] == "A" or e[0] == "B":
        print(f"* Pierwsza litera znaleziona w {e}")
        continue
    print(f"Sprawdzamy pierwszą literę w {e}")

print("===[koniec]===")
