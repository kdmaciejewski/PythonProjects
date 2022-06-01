def tabliczka(*args):
    lista = list()
    for i in args:
        for j in range(4):
            lista.append(i*j)

    return lista

def tabliczka_kwa(**kwaargs):
    lista = []
    for i in kwaargs.values():
        for j in range(4):
            lista.append(i*j)

    return lista


if __name__ == '__main__':

    print(tabliczka(1,2,3,4))
    print(tabliczka_kwa(a = 'a', b = 'b', c = 'c', d = 'd'))