# program r4_00.py
# sprawdzamy, czy posiadamy zainstalowane odpowiednie biblilteki zewnętrzne
# moduły json, datetime są wbudowane

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
