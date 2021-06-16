# program r6_01_csv_only.py
# tylko wczytywanie danych z pliku CSV

# wczytane dane będziemy zapisywać jako obiekty `list`
cities = []  # nazwy miejscowości
X = []  # szerokość geograficzna
Y = []  # długość geograficzna

# wczytujemy dane z pliku
with open("miasta.csv", "r", encoding='utf-8') as dane:
    cities_all = dane.readlines()

print(cities_all)

# czyścimy dane
for city in cities_all:
    datas = city.strip().split(
        ","
    )  # tu dzielimy tekst na elementy listy, znak `,` jest separatorem
    cities.append(datas[0])  # dodajemy do listy nazwę zmiejscowości
    X.append(float(datas[1]))  # i kolejne wartości współrzędnych
    Y.append(float(datas[2]))

# teraz zobaczymy nasze dane
print(cities, X, Y, sep="\n======\n")

# analogiczny efekt uzyskamy:
# print(cities)
# print("======")
# print(X)
# print("======")
# print(Y)
