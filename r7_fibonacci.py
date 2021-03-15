# program r7_fibonacci.py
# rekurencyjne obliczanie elementu ciągu Fibonacciego

def fib_rek(n):
    """Funkcja zwraca n-ty wyraz ciągu Fibonacciego."""
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

print(fib_rek(6))
