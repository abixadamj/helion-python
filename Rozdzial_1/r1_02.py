# program r1_02.py
import sys

print(f"Obecny system to {sys.platform}")
if sys.platform == "linux":
    print("Ten komunikat tylko dla Linux")
elif sys.platform == "darwin":
    print("Ten komunikat tylko dla Mac OS")
elif sys.platform == "win32":
    print("Ten komunikat tylko dla Windows")
else:
    print("Ten komunikat dla pozostałych systemów")
