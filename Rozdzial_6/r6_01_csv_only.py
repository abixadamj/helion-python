# program r6_01_csv_only.py
# Tylko wczytywanie danych z pliku CSV

# Wczytane dane będziemy zapisywać jako obiekty `list`
cities = []  # Nazwy miejscowości
X = []  # Szerokość geograficzna
Y = []  # Długość geograficzna

# Wczytujemy dane z pliku
with open("miasta.csv", "r", encoding='utf-8') as dane:
    cities_all = dane.readlines()

print(cities_all)

# Czyścimy dane
for city in cities_all:
    datas = city.strip().split(
        ","
    )  # Tu dzielimy tekst na elementy listy, znak `,` jest separatorem
    cities.append(datas[0])  # Dodajemy do listy nazwę zmiejscowości
    X.append(float(datas[1]))  # i kolejne wartości współrzędnych
    Y.append(float(datas[2]))

# Teraz zobaczymy nasze dane
print(cities, X, Y, sep="\n======\n")

# Analogiczny efekt uzyskamy stosując polecenia:
# print(cities)
# print("======")
# print(X)
# print("======")
# print(Y)
