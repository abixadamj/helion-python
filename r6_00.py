# program r6_00.py
# sprawdzamy moduł cartopy

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
