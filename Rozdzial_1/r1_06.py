# program r1_06.py
# Test modyfikacji obiektu typu list
list_object = [11, 22, 33, "A", "B", "C"]
print(f"Dla ID = {id(list_object)} wartość: {list_object}")

# Do obiektu możemy dodać wartość
list_object.append("Nowa")
print(f"Dla ID = {id(list_object)} wartość: {list_object}")
# lub zmienić wartość w środku
list_object[2] = "Inna wartość"
print(f"Dla ID = {id(list_object)} wartość: {list_object}")

# Test modyfikacji obiektu typu dict
dict_object = {1: "Pierwszy element"}
print(f"Dla ID = {id(dict_object)} wartość: {dict_object}")

# Do obiektu możemy dodać wartość
dict_object[2] = "Drugi element"
dict_object[3] = "Trzeci element"
print(f"Dla ID = {id(dict_object)} wartość: {dict_object}")

# lub zmienić wartość w środku
dict_object[2] = "Inna wartość"
print(f"Dla ID = {id(dict_object)} wartość: {dict_object}")
