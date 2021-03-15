# program r2_04.py
# wyświetlamy tło + obiekty

# wczytujemy moduł pgzrun
import pgzrun
from random import randint

# definiujemy klasy i funkcje dodatkowe

# start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"
# definiujemy wyświetlane obiekty i ich współrzędne X oraz Y
palette_a = Actor("palette.png")
palette_a.y = 10
palette_a.x = randint(70, 1210)
palette_b = Actor("palette.png")
palette_b.y = 843
palette_b.x = randint(70, 1210)
ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2

# najważniejsze funkcje sterujące
def update():
    pass


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


# uruchomienie modułu pygame zero
pgzrun.go()
