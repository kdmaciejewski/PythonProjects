import random


def log():
    print("Witaj w banku Santander Polska")

    pin = input('Podaj numer PIN ')


    print("Logowanie pomyślne")
    saldo = random.randint(0, 22000)

    while True:

        op = input("1 - Sprawdzenie salda\n2 - Wypłata gotówki\n3 - Wyjście\n")

        if (op == '1'):
            print('Saldo: ' + str(saldo))
        if (op == '2'):
            suma = int(input('Podaj sumę do wypłaty '))
            if suma > int(saldo):
                print("Niewstarczające saldo, nie można zrealizować transakcji")
                print('Brakuje: ' + str(suma - int(saldo)) + " zł")
            else:
                saldo -= suma
                print('Suma została wypłacona')

        if op == '3':
            print("Pomyślnie wylgogowano z systemu")
            break


if __name__ == '__main__':
    log()
