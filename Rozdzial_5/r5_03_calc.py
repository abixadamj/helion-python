# program r5_03_calc.py
# pandas i arkusz kalkulacyjny

import pandas as pd

# Zapasowa kopia do pobrania - stan na 16.06.2021 roku
# https://github.com/abixadamj/helion-python/raw/main/Rozdzial_5/dane_opady_temperatura.ods
source_data = "dane_opady_temperatura.ods"
print(f"Dane źródłowe: {source_data}")

# Tworzymy tzw. "DataFrame"
# Wymagany moduł odfpy
df = pd.read_excel(source_data, engine="odf")

# Wyświetlamy dane pobrane z sieci
print("----[ informacje o danych źródłowych ]---")
print(df)
print("----------------")

# Teraz dodamy kolumnę z wpisem tekstowym
df["Autor"] = "Adam Jurkiewicz"
print("----[ informacje o danych ]---")
print(df)

# Teraz próbujemy zapisać te dane do pliku
# Wymagany moduł openpyxl

# Libre Office Calc
df.to_excel("dane_opady_temperatura_nowy.ods", engine="odf")
# MS-Excel
df.to_excel("dane_opady_temperatura_nowy.xlsx", engine="openpyxl")
