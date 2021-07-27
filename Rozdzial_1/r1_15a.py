# program r1_15a.py
# Pętla while - wersja z wymuszeniem przerwania
a = 0
while a < 5:
    if a == 4:  # Kiedy a osiągnie wartość 4
        break  # przerywam pętlę while
    a += 1
    print(f"Aktualne a={a}")
# Koniec pętli
print(f"Ostatecznie a wynosi {a}")
