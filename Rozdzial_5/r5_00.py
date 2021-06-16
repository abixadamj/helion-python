# program r5_00.py
# pandas

from sys import exit

try:
    import pandas as pd

    print("Moduł pandas wczytany.")
except:
    print("Zainstaluj: 'pip install pandas' ")
    exit(0)

# jest ok, działamy dalej
source_data = "http://otwartedane.gdynia.pl/portal/data/city/6/3/data.csv"
print(f"Dane źródłowe: {source_data}")
