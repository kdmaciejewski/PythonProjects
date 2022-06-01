import random as r

def throw():
    suma1 = 0
    suma2 = 0
    list = []

    for i in range(4):
        val = r.randint(1, 6)
        list.append(val)
        suma1 += val

    for i in range(4):
        val = r.randint(1, 6)
        list.append(val)
        suma2 += val

    if suma1 > suma2:
        print("W turze 1 wyrzucono większą wartość równą " + str(suma1))
    else:
        print("W turze 2 wyrzucono większą wartość równą " + str(suma2))


if __name__ == '__main__':
    throw()