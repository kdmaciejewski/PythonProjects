class Calculator:
    __m = 0.3
    _kursEuro = 4.60
    _kursDolar = 4.20

    def __init__(self, *lista):
        self.__lista = lista

    def licz(self):
        for i in lista:
            print(i.getNazwa())
            self.cenaMarza(i.getCena())
            self.cenaEuro(i.getCena())
            self.cenaDolar(i.getCena())

    def cenaMarza(self, cena):
        print("Marża wynosi: " + str(round(cena * self.__m, 2)))

    def cenaEuro(self, cena):
        print("Cena w euro = " + str(round(cena / self._kursEuro, 2)))

    def cenaDolar(self, cena):
        print("Cena w dolarach = " + str(round(cena / self._kursDolar, 2)))

    def getLista(self):
        return self.__lista

    def setLista(self, lista):
        if isinstance(lista, list):
            self.__lista = lista
        else:
            raise TypeError('The attribute must be a list.')

class Produkt:
    def __init__(self, nazwa, cena):
        self.setNazwa(nazwa)
        self.__nazwa = nazwa
        self.setCena(cena)
        self.__cena = cena

    def setNazwa(self, imie):
        if isinstance(imie, str):
            self.__nazwa = imie
        else:
            raise TypeError('The attribute must be a string')

    def setCena(self, cena):
        if isinstance(cena, (int, float)):
            if cena > 0:
                self.__cena = cena
            else:
                raise ValueError('Price must be positive')
        else:
            raise TypeError('The attribute must be an int or a float')

    def getCena(self):
        return self.__cena
    def getNazwa(self):
        return self.__nazwa


    nazwa = property(getNazwa, setNazwa)
    cena = property(getCena, setCena)

if __name__ == '__main__':
    lista = []
    lista.append(Produkt('Bułka', 2))
    lista.append(Produkt('Ogórek', 5))
    lista.append(Produkt('Pizza Oetkera', 19))


    c = Calculator(lista)
    c.licz()

