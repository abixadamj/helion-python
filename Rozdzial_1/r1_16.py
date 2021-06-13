# program r1_16.py
# pętla while - nieskończone działanie z przerwaniem

from math import sin

X, Y = [], []
x, y = 0, 0

while True:
    x += 1
    X.append(x)
    y = sin(x * x)
    Y.append(y)
    if y > 0.99:
        print(f"Przerywamy dla y={y}")
        break
    print(f"Obliczony y={y}")

# ten kod zostanie wykonany po break
print(f"Lista X = {X}")
print(f"Lista Y = {Y}")
