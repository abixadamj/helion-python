# program r1_07.py
# Przykłady dla instrukcji warunkowych

test_object = 23
if test_object < 20:
    print("Niska wartość")
elif test_object < 30:
    print("Mniej niż 30")
elif test_object < 40:
    print("Mniej niż 40")
else:
    print("Żaden z powyższych.")

test_object = 43
if test_object < 20:
    print("Niska wartość")
elif test_object < 30:
    print("Mniej niż 30")
elif test_object < 40:
    print("Mniej niż 40")
else:
    print("Żaden z powyższych.")

test_object = "Adam"
if test_object == "Adam":
    print("Mamy test_object o wartości Adam")
else:
    print(f"Inna wartość => {test_object}.")

test_object = "adam"
if test_object == "Adam":
    print("Mamy test_object o wartości Adam")
else:
    print(f"Inna wartość => {test_object}.")
