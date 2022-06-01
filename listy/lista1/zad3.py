def mail_processing():
    lista = []
    for i in range(4):
        mail = input('Podaj email  ')
        lista.append(mail)

    a = len(lista)
    domeny = []

    for i in range(len(lista)):
        el = lista[i]       #pobieramy adres
        a = 0
        b = 0

        for j in range(len(el)):
            if el[j] == '@':
                a = j+1
            if el[j] == '.':
                b = j

        nazwa = el[a:b]
        if nazwa in domeny:
            for i in range(len(domeny)):
                if nazwa == domeny[i]:
                    domeny[i+1] += 1
        else:
            domeny.append(nazwa)
            domeny.append(1)

    print("Domena   Amount")
    for i in range(0, len(domeny), 2):
        print('{0:7s}  {1:6d}'.format(domeny[i], domeny[i+1]))


if __name__ == '__main__':
    mail_processing()