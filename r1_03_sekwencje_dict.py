# program r1_03_sekwencje_dict.py
# wyjątek przy odwoływaniu się do elementów słownika

slownik = {1: "Adam", 2: "Jurkiewicz", "S": "Linux"}
print(slownik)
print(type(slownik))

print("-------------------------------")

print("Badanie elementów: słownik")
print(len(slownik))
print(slownik[1])
print(slownik["S"])
print(slownik[4])
