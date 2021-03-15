# program r6_02_mapa.py
# podstawowa mapa

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

# wczytane dane będziemy zapisywać jako obiekty `list`
cities = []  # nazwy miejscowości
X = []  # szerokość geograficzna
Y = []  # długość geograficzna

# wczytujemy dane z pliku
with open("examples/miasta.csv", "r") as dane:
    cities_all = dane.readlines()

print(cities_all)

# czyścimy dane
for city in cities_all:
    datas = city.split(",")
    cities.append(datas[0].strip())
    X.append(float(datas[1]))
    Y.append(float(datas[2]))

# teraz zobaczymy nasze dane
print(cities, X, Y, sep="\n======\n")

# tworzymy okno
figure = plt.figure(figsize=(7, 5))
ax = figure.add_subplot(1, 1, 1, projection=crs.Mercator())  # dodajemy projekcję Merkatora

# dodajemy właściwość do mapy, zdjęcie
ax.stock_img()

# wyświetlamy okno
plt.show()
