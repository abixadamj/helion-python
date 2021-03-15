# program r1_32.py
# przestrzeń nazw - obiekty


class Klasa:
    wlasciwosc_0 = "X0"
    pass


obiekt_a = Klasa()
obiekt_b = Klasa()

obiekt_a.wlasciwosc_1 = "X1"
#
obiekt_b.wlasciwosc_2 = "X2"

print(dir(obiekt_a))
print("---------")
print(dir(obiekt_b))
print("---------")
print(obiekt_a.wlasciwosc_1)
print(obiekt_b.wlasciwosc_2)
print(obiekt_a.wlasciwosc_0)
print(obiekt_b.wlasciwosc_0)
# poniżej błędy
print("---------")
print(obiekt_a.wlasciwosc_2)
print(obiekt_b.wlasciwosc_1)
