# program r2_08.py
# Wyświetlamy tło + obiekty + ruch piłki
# Paletki „opakowujemy” w definicję klasy aby zmniejszyć ilość kodu
# Dodajemy ubsługę ruchu paletek + odbijanie piłeczki
# Aktualizujemy kod dla różnych wielkości paletki/piłeczki
# Dodajemy wygraną i koniec gry

# Wczytujemy moduł pgzrun
import pgzrun
from random import randint, choice

# Definiujemy klasę dla paletek
class Palette:
    def __init__(self, palette, position, width=140, ball_width=10):
        """Palette i jej właściwości"""
        self.palette = palette
        self.palette.x = position[0]
        self.palette.y = position[1]
        self.palette.speed = 5
        self.palette.pcenter = width // 2
        self.palette.ball_width = ball_width

    def drawing(self):
        """Wywołujemy metodę obiektu"""
        self.palette.draw()

    def move(self, direction):
        """Aktualizujemy pozycję w osi X"""
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < self.palette.pcenter:
                self.palette.x = self.palette.pcenter + 5
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - self.palette.pcenter):
                self.palette.x = WIDTH - self.palette.pcenter + 5

    def bounce(self):
        """Sprawdzamy czy piłeczka odbija się od paletki"""
        # Jeśli środek paletki zbyt daleko od środka piłeczki to nie odbijamy
        if (
            self.palette.distance_to(ball)
            > self.palette.pcenter + self.palette.ball_width
        ):
            return False

        # Jeśli środek paletki dalej niż 20 pixeli od środka piłeczki
        # w osi y to nie odbijamy
        if abs(self.palette.y - ball.y) > self.palette.ball_width * 2:
            return False

        # Dodatkowo zmieniamy kierunki lewo/prawo dla piłeczki
        if self.palette.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.palette.x < ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        # i odbijamy piłeczkę
        return True


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


def update_palettes():
    # Gracz_A
    if keyboard.a:
        palette_a.move("left")
    elif keyboard.s:
        palette_a.move("right")
    # Gracz_B
    if keyboard.k:
        palette_b.move("left")
    elif keyboard.l:
        palette_b.move("right")


def check_bounce():
    if palette_a.bounce():
        ball.direction_y = "down"
    if palette_b.bounce():
        ball.direction_y = "up"


def check_winner():
    if ball.winner:
        winner_txt = f"And the winner is: {ball.winner}"
        screen.draw.text(
            winner_txt, (WIDTH // 3, HEIGHT // 2), color="red", fontsize=60
        )


# Start programu
WIDTH = 1280
HEIGHT = 853
TITLE = "PONG - najlepsza gra na świecie ;-)"

# Definiujemy wyświetlane obiekty i ich współrzędne X oraz Y
palette_a = Palette(Actor("palette.png"), (randint(70, 1210), 10))
palette_b = Palette(Actor("palette.png"), (randint(70, 1210), 843))
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
    update_palettes()
    check_bounce()


def draw():
    screen.blit("nature-2384_1280.jpg", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()
    check_winner()


# Uruchomienie modułu Pygame Zero
pgzrun.go()
