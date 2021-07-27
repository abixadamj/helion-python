# program r1_24.py
# Rozbudowany sposób definiowania obiektu i metody


class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")

    def info(self):
        print(f"Kolor dla obiektu to: {self.kolor_obiektu}")

    def info_ex(self, nazwa):
        print(f"Kolor dla obiektu {nazwa} to: {self.kolor_obiektu}")


paletka_a = Paletka("czerwony")
paletka_b = Paletka("niebieski")
print("------------------------------------------")
print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
print(dir(paletka_a))
print("------------------------------------------")
print(f"Obiekt typu {type(paletka_b)} zawiera od razu pewne właściwości i metody:")
print(dir(paletka_b))
print("------------------------------------------")
print("Teraz sprawdzimy nasze właściwości:")
paletka_a.info()
paletka_b.info()
paletka_a.info_ex("a")
paletka_b.info_ex("b")
