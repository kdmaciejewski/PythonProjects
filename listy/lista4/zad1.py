class Dog:
    def __init__(self, imie, wiek, rasa):
        self.__imie = imie
        self.__wiek = wiek
        self.__rasa = rasa

    def print(self):
        print('Pies o imieniu: ' + self.__imie + ", w wieku: " + str(self.__wiek) + ", rasa: " + self.__rasa)

    @property
    def wiek(self):
        return self.__wiek

    @property
    def imie(self):
        return self.__imie

    @property
    def rasa(self):
        return self.__rasa

    @wiek.setter
    def wiek(self, wiek):
        if isinstance(wiek, (int, float)):
            if wiek > 0 and wiek < 50:
                self.__wiek = wiek
                print('Wiek został poprawnie zmieniony')
            else:
                raise ValueError('The attribute must be positive.')
        else:
            raise TypeError('The attribute must be an int or a float.')

    @imie.setter
    def imie(self, imie):
        if isinstance(imie, str):
            self.__imie = imie
        else:
            raise TypeError('The attribute must be a string.')
    @rasa.setter
    def rasa(self, rasa):
        if isinstance(rasa, str):
            self.__rasa = rasa
        else:
            raise TypeError('The attribute must be a string.')

    @rasa.deleter
    def rasa(self):
        print('Deleting...')
        del self.__rasa


if __name__ == '__main__':
    lista = []
    lista.append(Dog('Boryna', 5, 'Pitbull'))
    lista.append(Dog('Fafik', 4, 'Border'))
    lista.append(Dog('Bunia', 12, 'Hart'))
    lista.append(Dog('Ala', 1, 'Beagle'))

    for i in lista:
        i.print()

    setattr(lista[0], 'owner', 'Maria')
    setattr(lista[1], 'owner', 'Mati')
    setattr(lista[2], 'owner', 'Krzysztof')
    setattr(lista[3], 'owner', 'Franek')

    for i in lista:
        print('Pies o imieniu: ' + i.imie + ", w wieku: " + str(i.wiek) + ", rasa: " + i.rasa +
              ', właściciel: ' + i.owner)

    lista[1].wiek = 3
    del lista[1].rasa

    # for i in lista:
    #     print('Pies o imieniu: ' + i.imie + ", w wieku: " + str(i.wiek) + ", rasa: " + i.rasa +
    #           ', właściciel: ' + i.owner)