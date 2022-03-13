#from pakiet.calculate_module import add
import pakiet.calculate_module as p
import random as r

class Dice:
    def roll(self):
        # kostka = [1,2,3,4,5,6]
        # print(r.choice(kostka))
        print(r.randint(1,6))


class Animal:
    def __init__(self, imie):
        self.imie = imie

    def hau(self):
        for i in range(0, 6, 2):
            print(self.imie + ' hauuu')
            print(i)
            i += 2


class Dog(Animal):
    # tutaj trzeba dać słowo pass jeśli nic nie napiszemy, nie moze być pustej klasa
    def hau(self):
        i = 0
        while i < 3:
            print("woof")
            i += 1


if __name__ == '__main__':
    burek = Dog('Bunia')
    burek.hau()
    an = Animal("Malik")
    an.hau()
    p.add()
    d = Dice()
    d.roll()
