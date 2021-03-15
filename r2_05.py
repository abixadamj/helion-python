# program r2_05.py
# wyświetlamy tło + obiekty + ruch piłki

# wczytujemy moduł pgzrun
import pgzrun
from random import randint, choice

# definiujemy funkcje dodatkowe
def update_ball_position():
    # aktualizujemy pozycję w osi X
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    # aktualizujemy pozycję w osi Y
    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    # sprawdzamy, czy piłeczka "odbije się"
    # od lewej lub prawej krawędzi okna
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH - 5:
        ball.direction_x = "left"
    # sprawdzamy, czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "GRACZ B"
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"


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

# dodajemy własne właściwości
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 2
ball.winner = None

# najważniejsze funkcje sterujące
def update():
    update_ball_position()


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.draw()
    palette_b.draw()
    ball.draw()


# uruchomienie modułu pygame zero
pgzrun.go()
