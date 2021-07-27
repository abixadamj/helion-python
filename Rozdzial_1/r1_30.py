# program r1_30.py
# Przestrzeń nazw - funkcja i zmienna niemutowalna

zmienna_a = 10


def funkcja_A():
    print(f"Wewnątrz A: {zmienna_a} - ID = {id(zmienna_a)}")


def funkcja_B():
    zmienna_a = 20  # Przypisanie do zmiennej wewnątrz przestrzeni nazw!
    print(f"Wewnątrz B: {zmienna_a} - ID = {id(zmienna_a)}")


# Teraz test
print(f"Wartość początkowa: {zmienna_a} - ID = {id(zmienna_a)}")
#
funkcja_A()
#
funkcja_B()
#
print(f"Wartość końcowa: {zmienna_a} - ID = {id(zmienna_a)}")
