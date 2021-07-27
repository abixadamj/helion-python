# program r1_15f.py
# Pętla while - ciąg Fibonacciego

a, b = 0, 1
ciag = [a, b]
while a <= 400:
    a, b = b, a + b
    print(f"Aktualne wartości to a={a} | b={b}")
    ciag.append(b)
# Koniec pętli
print(ciag)
