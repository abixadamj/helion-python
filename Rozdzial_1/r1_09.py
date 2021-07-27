# program r1_09.py
# Przykłady dla instrukcji warunkowych

test_object = 13
print(f"test dla wartości = {test_object}")
if test_object < 40:
    print("Mniej niż 40")
    if test_object < 30:
        print("Mniej niż 30")
        if test_object < 20:
            print("Niska wartość")

test_object = 23
print(f"test dla wartości = {test_object}")
if test_object < 40:
    print("Mniej niż 40")
    if test_object < 20:
        print("Niska wartość")
        if test_object < 30:
            print("Mniej niż 30")
