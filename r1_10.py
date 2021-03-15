# program r1_10.py
# przykłady dla pętli for

test_object = "Autor - Adam Jurkiewicz"
print(f"Testujemy dla zmiennej typu: {type(test_object)}")
for litera in test_object:
    print(f"Litera {litera} ma wartość ASCII = {ord(litera)}")
print("===[koniec]===")

test_object = ["Adam", 3.14, (True, 33)]
print(f"Testujemy dla zmiennej typu: {type(test_object)}")
for e in test_object:
    print(f"Element {e} to typ = {type(e)}")
print("===[koniec]===")
