# program r1_27.py
# Klasy i ich ukryte właściwości - modyfikowanie


class Paletka:
    __rodzaj = "Paletka do Ping Ponga"
    ilosc = 0

    def __init__(self, kolor):
        self.kolor_obiektu = kolor
        print(f"Utworzyliśmy obiekt o kolorze: {self.kolor_obiektu} - ID: {id(self)}")
        Paletka.ilosc += 1

    def info(self):
        print(f"Kolor dla obiektu to: {self.kolor_obiektu}")
        print(f"W klasie: {Paletka.__rodzaj} jest elementów = {Paletka.ilosc}")

    def zmien_rodzaj(self, nowy_rodzaj):
        Paletka.__rodzaj = nowy_rodzaj


paletka_a = Paletka("czerwony")
paletka_a.info()
paletka_b = Paletka("niebieski")
paletka_b.info()
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
# Teraz wpisujemy nową wartość do właściwości klasy
paletka_a.zmien_rodzaj("Nowy rodzaj paletki")
#
paletka_a.info()
paletka_b.info()
