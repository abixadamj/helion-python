# program r1_23.py
# rozbudowany sposób definiowania obiektu


class Paletka:
    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")


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
print(f"Kolor dla a: {paletka_a.kolor_obiektu}")
print(f"Kolor dla b: {paletka_b.kolor_obiektu}")
