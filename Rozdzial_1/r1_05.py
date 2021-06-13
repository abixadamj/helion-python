# program r1_05.py
# test modyfikacji obiektu typu str
obiekt = "Adam"
print(id(obiekt))

# Do obiektu możemy przypisać inną wartość
obiekt = "Beata"
print(id(obiekt))

# możemy „zobaczyć” element obiektu
print(obiekt[3])

# ale nie możemy przypisać nic do elementu obiektu
# to polecenie generuje błąd
obiekt[3] = "X"
