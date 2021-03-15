# program r5_01_data_frame.py
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

# zapasowa kopia - stan na 4.03.2021 rok
# source_data = "https://raw.githubusercontent.com/abixadamj/project-simple/main/data.csv"
print(f"Dane źródłowe: {source_data}")

# tworzymy tzw. "DataFrame"
try:
    df = pd.read_csv(source_data)
    print("Pobrano dane źródłowe.")
except:
    print("UWAGA! wystąpił błąd.")
    exit(0)

# wyświetlamy dane w postaci pobranej z sieci
print("----[ informacje o danych źródłowych ]---")
print(df)
print("----------------")
