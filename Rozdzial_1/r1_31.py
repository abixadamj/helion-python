# program r1_31.py
# Przestrzeń nazw - funkcja i zmienna mutowalna

zmienna_a = [10]


def funkcja_A():
    print(f"Wewnątrz A: {zmienna_a} - ID = {id(zmienna_a)}")


def funkcja_B():
    zmienna_a[0] = 20  # Przypisanie do zmiennej poza przestrzenią nazw!
    print(f"Wewnątrz B: {zmienna_a} - ID = {id(zmienna_a)}")


# Teraz test
print(f"Wartość początkowa: {zmienna_a} - ID = {id(zmienna_a)}")
#
funkcja_A()
#
funkcja_B()
#
print(f"Wartość końcowa: {zmienna_a} - ID = {id(zmienna_a)}")
