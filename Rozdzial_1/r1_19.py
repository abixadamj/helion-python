# program r1_19.py
# funkcja do analizy ocen - kolejna wersja

import matplotlib.pyplot as plt


def srednia_ocen(oceny):
    if type(oceny) is not list:
        return f"Błędne dane wejściowe: {type(oceny)}"

    suma = sum(oceny)
    if oceny.count(5) > 4 or oceny.count(6) > 4:
        suma += 4

    srednia = suma / len(oceny)

    # rysujemy wykres kołowy z oceny
    legenda = ("1", "2", "3", "4", "5", "6")
    # budujemy listę ilości ocen od 1 do 6
    oceny_zliczone = [oceny.count(x) for x in range(1, 7)]
    #
    plt.pie(oceny_zliczone, labels=legenda)
    plt.show()

    return round(srednia, 2)


# sprawdzamy działanie funkcji
print(srednia_ocen("Błędne dane"))
print(
    srednia_ocen(
        [2, 3, 3, 4, 5, 1, 2, 2, 2, 3, 3, 6, 5, 5, 5, 4, 4, 4, 4, 1, 1, 3, 4, 2, 1]
    )
)
