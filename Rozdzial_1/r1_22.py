# program r1_22.py
# najprostszy sposób definiowania obiektu


class Paletka:
    pass


paletka_a = Paletka()

print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
print(dir(paletka_a))
