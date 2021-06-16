# program r5_03_calc.py
# pandas i arkusz kalkulacyjny

import pandas as pd

# zapasowa kopia do pobrania - stan na 16.06.2021 rok
# https://github.com/abixadamj/helion-python/raw/main/Rozdzial_5/dane_opady_temperatura.ods
source_data = "dane_opady_temperatura.ods"
print(f"Dane źródłowe: {source_data}")

# tworzymy tzw. "DataFrame"
# wymagany moduł odfpy
df = pd.read_excel(source_data, engine="odf")

# wyświetlamy dane w postaci pobranej z sieci
print("----[ informacje o danych źródłowych ]---")
print(df)
print("----------------")

# teraz dodamy kolumnę z wpisem tekstowym
df["Autor"] = "Adam Jurkiewicz"
print("----[ informacje o danych ]---")
print(df)

# teraz próbujemy zapisać te dane do pliku
# wymagany moduł openpyxl

# Libre Office Calc
df.to_excel("dane_opady_temperatura_nowy.ods", engine="odf")
# MS-Excel
df.to_excel("dane_opady_temperatura_nowy.xlsx", engine="openpyxl")
