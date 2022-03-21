# program r5_00.py
# pandas

import sys

try:
    import pandas as pd
    print("Moduł pandas wczytany.")
    import matplotlib.pyplot as plt
    print("Moduł matplotlib obecny.")
except ImportError as impErr:
    print("Brak modułu", impErr.args[0][16:].replace("'", ""))
    print("Zainstaluj: pip install", impErr.args[0][16:].replace("'", ""))
    sys.exit(0)

# Jest ok, działamy dalej
source_data = "http://otwartedane.gdynia.pl/portal/data/city/6/3/data.csv"
print(f"Dane źródłowe: {source_data}")
