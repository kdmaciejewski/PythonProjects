class Calculator:
    __m = 0.3
    _kursEuro = 4.60
    _kursDolar = 4.20

    def __init__(self, *lista):
        self.lista = lista

    def licz(self):
        for i in lista:
            print(i.nazwa)
            self.cenaMarza(i.cena)
            self.cenaEuro(i.cena)
            self.cenaDolar(i.cena)

    def cenaMarza(self, cena):
        print("Marża wynosi: " + str(round(cena * self.__m, 2)))

    def cenaEuro(self, cena):
        print("Cena w euro = " + str(round(cena / self._kursEuro, 2)))

    def cenaDolar(self, cena):
        print("Cena w dolarach = " + str(round(cena / self._kursDolar, 2)))

class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


if __name__ == '__main__':
    lista = []
    lista.append(Produkt('Bułka', 2))
    lista.append(Produkt('Ogórek', 5))
    lista.append(Produkt('Pizza Oetkera', 19))


    c = Calculator(lista)
    c.licz()

