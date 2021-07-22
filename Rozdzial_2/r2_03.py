# program r2_03.py
# Wyświetlamy tło + obiekty

# Wczytujemy moduł pgzrun
import pgzrun

# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"
# Definiujemy wyświetlane obiekty i ich współrzędne Y
palette_a = Actor("palette.png")
palette_a.y = 10
palette_b = Actor("palette.png")
palette_b.y = 843
ball = Actor("ball.png")
ball.y = HEIGHT // 2

# Najważniejsze funkcje sterujące
def update():
    pass


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


# Uruchomienie modułu Pygame Zero
pgzrun.go()
