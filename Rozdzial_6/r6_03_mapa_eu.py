# program r6_03_mapa_eu.py
# Mapa Europy

from sys import exit

try:
    import cartopy.crs as crs
    import cartopy.feature as cfeature

    print("Moduł cartopy wczytany.")
except:
    print("Zainstaluj: 'pip install cartopy' ")
    exit(0)

try:
    import matplotlib.pyplot as plt

    print("Moduł matplotlib wczytany.")
except:
    print("Zainstaluj: 'pip install matplotlib' ")
    exit(0)

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
    datas = city.strip().split(",")
    cities.append(datas[0])
    X.append(float(datas[1]))
    Y.append(float(datas[2]))

# Teraz zobaczymy nasze dane
print(cities, X, Y, sep="\n======\n")

# Tworzymy okno
figure = plt.figure(figsize=(7, 5))
ax = figure.add_subplot(
    1, 1, 1, projection=crs.Mercator()
)  # Dodajemy projekcję Merkatora

# Dodajemy właściwość do mapy - zdjęcie
ax.stock_img()

# Wydzielamy tylko wycinek mapy - Europę
ax.set_extent([-10, 35, 66, 34], crs=crs.PlateCarree())

# Wyświetlamy okno
plt.show()
