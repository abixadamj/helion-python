# program r2_05.py
# Wyświetlamy tło + obiekty + ruch piłki

# Wczytujemy moduł pgzrun
import pgzrun
from random import randint, choice

# Definiujemy funkcje dodatkowe
def update_ball_position():
    # Aktualizujemy pozycję w osi X
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    # Aktualizujemy pozycję w osi Y
    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    # Sprawdzamy, czy piłeczka "odbije się"
    # od lewej lub prawej krawędzi okna
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"
    # Sprawdzamy, czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "GRACZ B"
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"


# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

# Definiujemy wyświetlane obiekty i ich współrzędne X oraz Y
palette_a = Actor("palette.png")
palette_a.y = 10
palette_a.x = randint(70, 1210)
palette_b = Actor("palette.png")
palette_b.y = 843
palette_b.x = randint(70, 1210)
ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2

# Dodajemy własne właściwości
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 2
ball.winner = None

# Najważniejsze funkcje sterujące
def update():
    update_ball_position()


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


# Uruchomienie modułu Pygame Zero
pgzrun.go()
