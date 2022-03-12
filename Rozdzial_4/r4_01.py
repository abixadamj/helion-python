# program r4_01.py
# Sprawdzamy, czy mamy zainstalowane odpowiednie biblilteki zewnętrzne
# Importujemy funkcje dodatkowe

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
