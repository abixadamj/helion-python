# program r2_02.py
# Wyświetlamy tło

# Wczytujemy moduł pgzrun
import pgzrun

# Definiujemy klasy i funkcje dodatkowe

# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

# Najważniejsze funkcje sterujące
def update():
    pass


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))


# Uruchomienie modułu Pygame Zero
pgzrun.go()
