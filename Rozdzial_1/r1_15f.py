# program r1_15f.py
# pętla while - ciąg Fibonacciego

a, b = 0, 1
ciag = [a, b]
while a <= 400:
    a, b = b, a + b
    print(f"Aktualne wartości to a={a} | b={b}")
    ciag.append(b)
# koniec pętli
print(ciag)
