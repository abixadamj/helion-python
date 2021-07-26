# program r6_01_read.py
# Wczytujemy dane do wyświetlenia

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
