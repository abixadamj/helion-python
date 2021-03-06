# program r4_00.py
# Sprawdzamy, czy mamy zainstalowane odpowiednie biblilteki zewnętrzne
# Moduły json i datetime są wbudowane

try:
    import numpy as np

    print("OK, mamy moduł numpy.")
except:
    print("Brak modułu numpy.")

try:
    import matplotlib

    print("OK, mamy moduł matplotlib.")
except:
    print("Brak modułu matplotlib.")

try:
    from astropy.time import Time

    print("OK, mamy moduł astropy.")
except:
    print("Brak modułu astropy.")


try:
    from astroquery.jplhorizons import Horizons

    print("OK, mamy moduł astroquery.")
except:
    print("Brak modułu astroquery.")
