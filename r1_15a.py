# program r1_15a.py
# pętla while - wersja z wymuszeniem przerwania
a = 0
while a < 5:
    if a == 4:  # kiedy a osiągnie wartość 4
        break  # przerywam pętlę while
    a += 1
    print(f"Aktualne a={a}")
# koniec pętli
print(f"Ostatecznie a wynosi {a}")
