class Dog:
    def __init__(self, imie, wiek, rasa):
        self.imie = imie
        self.wiek = wiek
        self.rasa = rasa

    def print(self):
        print('Pies o imieniu: ' + self.imie + ", w wieku: " + str(self.wiek) + ", rasa: " + self.rasa)

    def setWiek(self, wiek):
        if isinstance(wiek, int):
            self.wiek = wiek
        print('Wiek został poprawnie zmieniony')
        self.print()


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

    lista[1].setWiek(3)