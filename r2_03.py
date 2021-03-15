# program r2_03.py
# wyświetlamy tło + obiekty

# wczytujemy moduł pgzrun
import pgzrun

# start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"
# definiujemy wyświetlane obiekty i ich współrzędne Y
palette_a = Actor("palette.png")
palette_a.y = 10
palette_b = Actor("palette.png")
palette_b.y = 843
ball = Actor("ball.png")
ball.y = HEIGHT // 2

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
