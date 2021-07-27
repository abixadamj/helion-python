# program r1_02.py
import sys

print(f"Obecny system to {sys.platform}")
if sys.platform == "linux":
    print("Komunikat tylko dla Linux")
elif sys.platform == "darwin":
    print("Komunikat tylko dla Mac OS")
elif sys.platform == "win32":
    print("Komunikat tylko dla Windows")
else:
    print("Komunikat dla pozostałych systemów")
