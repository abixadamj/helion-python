# program r4_04_callable.py
# przykład funkcji przekazywanej jako parametr, tzw. typ function


def dodawanie(a, b):
    return a + b


def mnozenie(a, b):
    return a * b


def operacja(rodzaj, par_1, par_2):
    wynik = rodzaj(par_1, par_2)
    return wynik


wynik_1 = operacja(dodawanie, 2, 3)
print(f"Wynik dodawania: {wynik_1}")

wynik_2 = operacja(mnozenie, 2, 3)
print(f"Wynik mnożenia: {wynik_2}")

print(f"Typ funkcji dodawania = {type(dodawanie)}")
print(f"Czy funkcja wykonywalna = {callable(dodawanie)}")

print(f"Typ funkcji mnozenia = {type(mnozenie)}")
print(f"Czy funkcja wykonywalna = {callable(mnozenie)}")
