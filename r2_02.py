# program r2_02.py
# wyświetlamy tło

# wczytujemy moduł pgzrun
import pgzrun

# definiujemy klasy i funkcje dodatkowe

# start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

# najważniejsze funkcje sterujące
def update():
    pass


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))


# uruchomienie modułu pygame zero
pgzrun.go()
