class Monster:
    count = 0
    def __init__(self, nazwa, sila, wiek, typ, poziom = 0):
        self.nazwa = nazwa
        self.__nazwa = nazwa
        self.sila = sila
        self.__sila = sila
        self.poziom = poziom
        self.__poziom = poziom
        self.wiek = wiek
        self.__wiek = wiek
        self.typ = typ
        self.__typ = typ
        Monster.count += 1

    def atak(self, otherMonster):
        print("Potwór " + self.nazwa + ' atakuje ' + otherMonster.nazwa)
        del otherMonster

    def przygotowanie(self):
        print("Potwór " + self.nazwa + ' przygotowuje się do ataku!')

    def print(self):
        print("Potwór " + self.nazwa + ', poziom: ' + str(self.poziom))

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, value):
        if isinstance(value, str):
            self.__nazwa = value
        else:
            raise TypeError('The atrribute must have type string')

    @property
    def sila(self):
        return self.__sila

    @sila.setter
    def sila(self, value):
        if isinstance(value, str):
            self.__sila = value
        else:
            raise TypeError('The atrribute must have type string')

    @property
    def poziom(self):
        return self.__poziom

    @poziom.setter
    def poziom(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__poziom = value
            else:
                raise ValueError("Poziom must be positive")
        else:
            raise TypeError('The atrribute must have type int')

    @property
    def wiek(self):
        return self.__wiek

    @wiek.setter
    def wiek(self, value):
        if isinstance(value, int):
            if value > 0:
                self.__wiek = value
            else:
                raise ValueError("Age must be positive")
        else:
            raise TypeError('The atrribute must have type int')

    @property
    def typ(self):
        return self.__typ

    @typ.setter
    def typ(self, value):
        if isinstance(value, str):
            self.__typ = value
        else:
            raise TypeError('The atrribute must have type string')

class Game:
    def __init__(self, nazwa, *postacie):
        self.__nazwa = nazwa
        self.__postacie = postacie

    def play(self):
        for i in self.postacie:
            i.print()
            i.przygotowanie()

        self.postacie[0].atak(self.postacie[1])

    @property
    def nazwa(self):
        return self.__nazwa

    @nazwa.setter
    def nazwa(self, val):
        self.__nazwa = val

    @nazwa.deleter
    def nazwa(self):
        print('Usuwanie nazwy gry...')
        del self.__nazwa

    @property
    def postacie(self):
        return self.__postacie

    @postacie.setter
    def postacie(self, val):
        self.__postacie = val

    @postacie.deleter
    def postacie(self):
        print('Usuwanie postaci...')
        del self.__postacie


if __name__ == '__main__':
    p1 = Monster('Smok', 'Ogień', 300, 'Gad', 42)
    p2 = Monster('Beduin', 'Piasek', 52, 'Człowiekowaty', 14)
    p3 = Monster('Waran z Komodo', "Jad", 233, "Gad", 11)

    l = [p1, p2, p3]
    print('Liczba utworzonych potworów: ' + str(Monster.count))

    g = Game('Gotik', p1, p2, p3)
    g.play()

