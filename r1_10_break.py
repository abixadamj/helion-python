# program r1_10_break.py
# przykłady dla pętli for i break

test_object = ["Adam", "Beata", "Szymon", "Artur", "Magda"]
print(f"Testujemy dla obiektu: {test_object}")

for e in test_object:
    if e == "Szymon":
        print("* Znaleźliśmy Szymona!")
        break
    print(f"Element: {e} ")

print("===[koniec]===")
