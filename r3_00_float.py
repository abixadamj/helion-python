# program r3_00_float.py
# pierwsze wczytywanie danych i walidacja

# definiujemy funkcję wczytującą dane
def read_datas():
    h_start = float(input("Teraz podaj wysokość początkową (w metrach): "))
    v_start = float(input("teraz podaj prędność początkową (w m/sek) :"))

    if h_start < 10:
        print("Niestety, wysokość zbyt niska (min. 10m)!")
        return None

    if v_start < 2:
        print("Niestety, prędkość początkowa zbyt niska (min. 2 m/s)!")
        return None

    return (h_start, v_start)


initial_values = None
while initial_values is None:
    print("Proszę, podaj dane niezbędne dla wykresu.")
    initial_values = read_datas()

print("OK, dane początkowe wczytane - działamy dalej.")
