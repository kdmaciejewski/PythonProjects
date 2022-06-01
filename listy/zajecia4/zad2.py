class Animal:
    def __init__(self, imie):
        self._imie = imie

    def przedstawSie(self):
        print("Zwierzę o imieniu: " + self._imie, end=' ')

class Psowate(Animal):
    def __init__(self, imie, rasa, kolor):
        super().__init__(imie)
        self._rasa = rasa
        self._kolor = kolor

    def przedstawSie(self):
        super().przedstawSie()
        print(" rasa: " + self._rasa, end=' ')

class Kotowate(Animal):
    def __init__(self, imie, rodzaj):
        super().__init__(imie)
        self._rodzaj = rodzaj

    def przedstawSie(self):
        super().przedstawSie()
        print(" rasa: " + self._rasa, end=' ')

class Pitbull(Psowate):
    def __init__(self, imie, rasa, kolor, czyNiebezpieczny):
        super().__init__(imie, rasa, kolor)
        self._czyNiebezpieczny = czyNiebezpieczny

    def przedstawSie(self):
        super(Psowate, self).przedstawSie()
        print(" czyNiebezpieczny: " + str(self._czyNiebezpieczny), end=' ')

class Border(Psowate):
    def __init__(self,imie, rasa, kolor, inteligencja):
        super().__init__(imie, rasa, kolor)
        self._inteligencja = inteligencja

    def przedstawSie(self):
        super(Psowate, self).przedstawSie()
        print(" o inteligencji: " + str(self._inteligencja), end=' ')
class Owczarek(Psowate):
    def __init__(self, imie, rasa, kolor, sila):
        super().__init__(imie, rasa, kolor)
        self._sila = sila

    def przedstawSie(self):
        super().przedstawSie()
        print(" o sile: " + str(self._sila), end=' ')


    def getSila(self):
        return self._sila


class Sfinks(Kotowate):
    def __init__(self, imie, rodzaj, pochodzenie):
        super().__init__(imie, rodzaj)
        self._pochodzenie = pochodzenie

    def przedstawSie(self):
        super(Kotowate, self).przedstawSie()
        print(" pochodzi z: " + str(self._pochodzenie), end=' ')

class Dachowiec(Kotowate):
    def __init__(self, imie, rodzaj, czyZdrowy):
        super().__init__(imie, rodzaj)
        self.czyZdrowy = czyZdrowy

    def przedstawSie(self):
        super(Kotowate, self).przedstawSie()
        print(" czyZdrowy: " + str(self._czyZdrowy), end=' ')

class Tygrys(Kotowate):
    def __init__(self, imie, rodzaj, sila):
        super().__init__(imie, rodzaj)
        self.sila = sila

    def przedstawSie(self):
        super(Kotowate, self).przedstawSie()
        print(" o sile: " + str(self._sila), end=' ')

if __name__ == '__main__':
    a = Owczarek('Burek', 'Owczarek niemiecki', 'brązowy', 70)
    a.przedstawSie()
    print()
    print(a.getSila())
    b = Psowate('Bunia', 'Beagle', 'biały')
    print()
    b.przedstawSie()
    #help(b)