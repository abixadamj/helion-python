# program r4_03.py
# Sprawdzamy, czy mamy zainstalowane odpowiednie biblilteki zewnętrzne
# Importujemy funkcje dodatkowe
# Wprowadzamy kod z projektu https://github.com/chongchonghe/Python-solar-system

from sys import exit
from r4_functions import *

try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import numpy as np
    from astropy.time import Time
    from astroquery.jplhorizons import Horizons
    ok_module_info(["matplotlib", "astropy", "astroquery"])
except ImportError as impErr:
    load_module_ok = error_module_info(impErr.args[0])
    print("Niestety, wystąpiły błędy.")
    print("Nie mogę dalej działać.")
    exit(0)

nasaids = [1, 2, 3, 4]  # Numery ID w bazie NASA
names = ["Merkury", "Wenus", "Ziemia", "Mars"]
colors = ["gray", "orange", "green", "chocolate"]
sizes = [0.38, 0.95, 1.0, 0.53]
texty = [0.47, 0.73, 1, 1.5]
planet_datas = get_horizon_data(nasaids, names, colors, sizes)

# Tworzymy obiekt ax, który będzie "oknem" do wyświetlenia animacji
plt.style.use("dark_background")
fig = plt.figure(
    planet_datas["info"], figsize=[8, 8]
)  # Fragment kodu wyżej definiuje tytuł i rozmiar okna
ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))

# Wyświetlamy okno
plt.show()
