# program r4_01.py
# sprawdzamy, czy posiadamy zainstalowane odpowiednie biblilteki zewnętrzne
# importujemy funkcje dodatkowe

from sys import exit
from r4_functions import *

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
