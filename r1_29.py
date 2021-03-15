# program r1_29.py
# klasy - program przykładowy


class Paletka:
    ilosc = 0
    __producent = "Firma A"

    def __init__(self, kolor, rozmiar, nazwa="Nazwa domyślna"):
        self.kolor_obiektu = kolor
        self.rozmiar_obiektu = rozmiar
        self.nazwa_obiektu = nazwa
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")
        Paletka.ilosc += 1

    def __del__(self):
        # destruktor
        Paletka.ilosc -= 1

    def info(self):
        print("----------------------------------------------------------------")
        print(
            f"Kolor dla obiektu o nazwie {self.nazwa_obiektu} to: {self.kolor_obiektu}"
        )
        print(f"Rozmiar tego obiektu wynosi: {self.rozmiar_obiektu}")
        print(f"W klasie jest elementów = {Paletka.ilosc}")


paletka_a = Paletka("czerwony", "xl", "Strong")
paletka_b = Paletka("niebieski", "xl")
paletka_c = Paletka("żółty", "xxl", "Extra")
paletka_d = Paletka("czerwony", "s", "S-Strong")
paletka_e = Paletka("czerwony", "xl")
paletka_a.info()
paletka_b.info()
paletka_c.info()
paletka_d.info()
paletka_e.info()
#
del paletka_b
del paletka_d
#
paletka_a.info()
paletka_c.info()
paletka_e.info()
