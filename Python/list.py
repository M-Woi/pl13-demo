lista_1 = ['pomidorowa', 'ogórkowa', 'rosół', 'pieczarkowa']

print(lista_1[-1])
print(lista_1[0])
print(lista_1[1])
print(lista_1[2])
print(lista_1[3])
print(lista_1[4])

class MojaKlasa:
    def __init__(self):
        self.publiczna_zmienna = 42
        self._nieoficjalna_zmienna = "To jest nieoficjalna zmienna"

    def metoda(self):
        inna_zmienna = "Inna zmienna"
        print(self.publiczna_zmienna)
        print(self._nieoficjalna_zmienna)
        print(inna_zmienna)

moj_obiekt = MojaKlasa()
print(moj_obiekt.publiczna_zmienna)  # Wyświetli 42
print(moj_obiekt._nieoficjalna_zmienna)  # Wyświetli "To jest nieoficjalna zmienna"
moj_obiekt.metoda()

sheep_array.count