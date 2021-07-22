# program r3_00.py
# Pierwsze wczytywanie danych i walidacja

# Definiujemy funkcję wczytującą dane
def read_datas():
    h_start = input("Teraz podaj wysokość początkową (w m): ")
    v_start = input("Teraz podaj prędkość początkową (w m/sek) :")

    if h_start < 10:
        print("Niestety, wysokość zbyt niska (min. 10 m)!")
        return None

    if v_start < 2:
        print("Niestety, prędkość początkowa zbyt niska (min. 2 m/s)!")
        return None

    return (h_start, v_start)


initial_values = None
while initial_values is None:
    print("Proszę, podaj dane niezbędne do wygenerowania wykresu.")
    initial_values = read_datas()

print("OK, dane początkowe wczytane - działamy dalej.")
