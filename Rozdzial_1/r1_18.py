# program r1_18.py
# Funkcja do analizy ocen - kolejna wersja


def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f"Błędne dane wejściowe: {type(oceny)}"

    suma = sum(oceny)
    if oceny.count(5) > 4 or oceny.count(6) > 4:
        suma += 4

    srednia = suma / len(oceny)

    return round(srednia, 2)


# Sprawdzamy działanie funkcji
print(srednia_ocen("Błędne dane"))
print(srednia_ocen([2, 3, 3, 4, 5, 3, 4, 2, 1]))
print(srednia_ocen([5, 5, 5, 1, 2, 1]))
print(srednia_ocen([5, 5, 5, 1, 2, 1, 5, 5]))
