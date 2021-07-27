# program r1_17p.py
# Pierwsza funkcja - parametry i ich ID


def test_id(parametr):
    print("-[ test wewnątrz funkcji ]-")
    print(f"Parametr ID = {id(parametr)}")
    print(f"Parametr type = {type(parametr)}")
    print(f"Parametr = {parametr}")


# Sprawdzamy działanie funkcji i ID obiektu

obiekt_1 = "TEST A"
print(f"ID obiekt_1 = {id(obiekt_1)}")
test_id(obiekt_1)
print("#################################")
#
obiekt_2 = [1, 2, 3]
print(f"ID obiekt_2 = {id(obiekt_2)}")
test_id(obiekt_2)
print("#################################")
#
obiekt_3 = {1: "TEST"}
print(f"ID obiekt_3 = {id(obiekt_3)}")
test_id(obiekt_3)
print("#################################")
