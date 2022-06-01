import sys


def logowanie():
    users = {}

    while True:
        try:
            op = int(input("Jaką operację chcesz wykonać?\n1 - Zaloguj\n2 - Zarejestruj\n3 - Wyświetl użytkowników\n4 - Zakończ\n"))

            if op == 1:
                n = input("Podaj nick ")
                if n in users.keys():
                    print("Zalogowano pomyślnie!")

                else:
                    print("Błędne dane logowania")

            elif op == 2:
                print('Witaj! Żeby założyc konto podaj adres imie, nazwisko i adres email ')
                imie = input('Podaj imie ')
                nazwisko = input('Podaj nazwisko ')
                mail = input('Podaj adres email ')
                nick = input('Podaj nick ')

                while nick in users:

                    print('Ten nick jest już zajęty')
                    nick = input('Podaj inny nick ')

                users[nick] = (imie, nazwisko, mail)
                print("Twoje konto zostało założone")
                print("Konieczne jest założenie maila z domeną @pwr.edu.pl")

                pwr_mail = imie + "." + nazwisko + "@pwr.edu.pl"

                print('Mail politechniczny został utworzony')
                print('Twój mail to: ' + pwr_mail)
                users[nick] = (imie, nazwisko, pwr_mail)

            elif op == 3:
                for i, j in users.items():
                    print(i, j)
                print(users.items())

            elif op == 4:
                break

            else:
                raise ValueError('Wprowadzono złą wartość operacji')

        except ValueError as val:
            print(val, sys.exc_info()[0])


if __name__ == '__main__':
    logowanie()
