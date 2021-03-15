# program r4_03.py
# sprawdzamy, czy posiadamy zainstalowane odpowiednie biblilteki zewnętrzne
# importujemy funkcje dodatkowe
# wprowadzamy kod z projektu https://github.com/chongchonghe/Python-solar-system

from sys import exit
from r4_functions import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import date, datetime, timedelta
import numpy as np


class Planet:  # definiujemy poszczególne planety
    def __init__(self, name, rad, color, r, v):
        self.name = name
        self.r = np.array(r, dtype=np.float)  # wektory promienia odległości od Słońca
        self.v = np.array(v, dtype=np.float)  # wektory prędkości względem Słońca
        self.xs = []  # kolejne pozycje X
        self.ys = []  # kolejne pozycje Y
        # właściwości odwołujące się do okna z animacją
        self.plot = ax.scatter(
            r[0], r[1], color=color, s=rad ** 2, edgecolors=None, zorder=10
        )
        (self.line,) = ax.plot([], [], color=color, linewidth=1.4)


class SolarSystem:
    def __init__(self):
        self.planets = []
        self.time = None
        # właściwość
        self.timestamp = ax.text(
            0.03, 0.94, "Data: ", color="w", transform=ax.transAxes, fontsize="x-large"
        )

    def add_planet(self, planet):
        # dodajemy planetę
        self.planets.append(planet)

    def evolve(self):
        # obliczamy kolejne punkty trajektorii
        dt = 1
        self.time += timedelta(dt)
        plots = []
        lines = []
        for i, planet in enumerate(self.planets):
            # obliczamy kolejne wektory promienia
            planet.r += planet.v * dt
            # obliczamy przyspieszenie liczone w jednostkach astronomicznych
            # np.sum() -> https://numpy.org/doc/stable/reference/generated/numpy.sum.html
            # GM można wyrazić w m/s², a możemy też jako AU/day²
            # M to masa Słońca, około 333 000 razy większa od masy Ziemi (ok. 2×10^30 kg.)
            # masy planet są zakładane jako pomijalne,
            # G - stała grawitacyjna, nie mylić z przyspieszeniem ziemskim g
            # sum(r²)^½ to długość wektora
            acc = -2.959e-4 * planet.r / np.sum(planet.r ** 2) ** (3 / 2)  # AU/day^2
            # obliczamy kolejne wektory prędkości
            planet.v += acc * dt
            # w tym momencie korzystamy z właściwości mutable dla self.planets
            # dodajemy pozycje X, Y i przesunięcie wykresu
            planet.xs.append(planet.r[0])
            planet.ys.append(planet.r[1])
            # dodajemy kolejny element animacji
            planet.plot.set_offsets(planet.r[:2])
            plots.append(planet.plot)
            planet.line.set_xdata(planet.xs)
            planet.line.set_ydata(planet.ys)
            # dodajemy kolejny odcinek linii
            lines.append(planet.line)
        # dodajemy zabezpieczenie przed zbyt dużą ilością obliczeń, max. 10000 pozycji
        if len(planet.xs) > 10000:
            raise SystemExit("Aby zapobiec przepełnieniu pamięci RAM")

        # ustawiamy tekst daty na kolejny dzień
        self.timestamp.set_text(f"Data: {self.time.isoformat()}")
        # zwracamy wartości niezbędne do zbudowania animacji
        return plots + lines + [self.timestamp]


load_module_ok = True

try:
    import numpy as np

    ok_module_info("numpy")
except:
    error_module_info("numpy")
    load_module_ok = False

try:
    import matplotlib

    ok_module_info("matplotlib")
except:
    err_module_info("matplotlib")
    load_module_ok = False

try:
    from astropy.time import Time

    ok_module_info("astropy")
except:
    error_module_info("astropy")
    load_module_ok = False


try:
    from astroquery.jplhorizons import Horizons

    ok_module_info("astroquery")
except:
    error_module_info("astroquery")
    load_module_ok = False

if not load_module_ok:
    print("Niestety, wystąpiły błędy.")
    print("Nie mogę dalej działać.")
    exit(0)

# teraz mamy wszystkie moduły zainstalowane
print("Super! Możemy działać....")

nasaids = [1, 2, 3, 4]  # numery ID w bazie NASA
names = ["Merkury", "Wenus", "Ziemia", "Mars"]
colors = ["gray", "orange", "green", "chocolate"]
sizes = [0.38, 0.95, 1.0, 0.53]
texty = [0.47, 0.73, 1, 1.5]
planet_datas = get_horizon_data(nasaids, names, colors, sizes)

# tworzymy obiekt ax, który będzie "oknem" do wyświetlenia animacji
plt.style.use("dark_background")
fig = plt.figure(
    planet_datas["info"], figsize=[8, 8]
)  # to definiuje tytuł rozmiar okna
ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))

# tworzymy układ słoneczny bazując na Słońcu + 4 planetach
# wywołujemy klasę Planet dla Słońca tylko aby zadziałał konstruktor
Planet("Słońce", 28, "yellow", [0, 0, 0], [0, 0, 0])
# stowrzymy obiekt klasy Systemu Słonecznego
solar_system = SolarSystem()

# ustawiamy czas początkowy
solar_system.time = datetime.strptime(planet_datas["date"], "%Y-%m-%d").date()

# generujemy dane do animacji
for nasaid in nasaids:
    planet = planet_datas[nasaid]

    # dodajemy planetę do układu słonecznego
    solar_system.add_planet(
        Planet(
            planet["name"],
            planet["size"] * 20,
            planet["color"],
            planet["r"],
            planet["v"],
        )
    )

    # dodajemy do okna animacji nazwę planety
    ax.text(
        0,
        -(texty[nasaid - 1] + 0.1),
        planet["name"],
        color=planet["color"],
        zorder=1000,
        ha="center",
        fontsize="large",
    )


# definiujemy funkcję, którą wywołamy z animation.FuncAnimation()
def animate(i):
    return solar_system.evolve()


# wykonujemy animację
solar_animation = animation.FuncAnimation(
    fig,
    animate,
    repeat=False,
    frames=365,
    blit=True,
    interval=10,
)

# wyświetlamy okno
plt.show()
