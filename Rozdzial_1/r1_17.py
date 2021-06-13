# program r1_17.py
# pierwsza funkcja do analizy ocen


def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f"Błędne dane wejściowe: {type(oceny)}"

    srednia = sum(oceny) / len(oceny)

    return round(srednia, 2)


# sprawdzamy działanie funkcji
print(srednia_ocen("Błędne dane"))
print(srednia_ocen([2, 3, 3, 4, 5, 3, 4, 2, 1]))
print(srednia_ocen([5, 5, 5, 1, 2, 1]))
print(srednia_ocen([5, 5, 5, 1, 2, 1, 5, 5]))
