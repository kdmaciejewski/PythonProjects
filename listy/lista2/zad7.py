import time
import os

def catalog():
    c = input('Wprowadź ścieżkę katalogu ')

    if os.path.isdir(c):
        f = input('Wprowadź nazwę pliku ')
        filepath = os.path.join(c, f)

         # Data ostatniej modyfikacji
        print(time.localtime(os.path.getmtime(filepath)))

        # Data utworzenia
        print(time.localtime(os.path.getctime(filepath)))

        # Data ostatniego dostępu
        print(time.localtime(os.path.getatime(filepath)))

        print(os.path.getsize(filepath))

    else:
        print("Ten katalog nie istnieje")


if __name__ == '__main__':
    catalog()