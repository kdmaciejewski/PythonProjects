import random

class Point:
    def __init__(self, *args):
        ar = []
        for i in args:
            if isinstance(i, int):
                ar.append(i)
            else:
                raise TypeError('Podano zły typ wartości dla współrzędnych')

        self._args = ar

    def __len__(self):
        return len(self._args)


    def __repr__(self):
        s = "Point: "
        for i in self._args:
            s += str(i)
            s += " "
        return s

    def losuj(self):
        liczba = int(input('Podaj liczbę argumentów '))
        lista = []
        for i in range(liczba):
            lista.append(random.randint(-100, 100))

        print('Punkt: ' + str(tuple(lista)))


if __name__ == '__main__':
    p = Point(1,2,3)
    p2 = Point(1,2)
    p4 = Point(1,2,4,5)
    p5 = Point(1,2,4,5,6)
    print(p)
    print(len(p))
    print(p2)
    print(p4)
    print(p5)

    p.losuj()