import time
import os

def catalog():
    currentDir = os.getcwd()
    print(currentDir)
    filename = "scripts.txt"
    fullpath = os.path.join(currentDir, filename)
    print(fullpath)

    #Ścieżka względna - okresla położenie pliku względem bieżącego katalogu.
    print('eeeeeeeeeeeeeeeeeeee')
    print(os.path.abspath('zad7.py') )               #Podaj nazwę pliku na Twoim dysku  - przekazujesz względną ścieżkę dostępu do plik, funkcja poda bezwględną.
    #Ścieżka bezwzględna

    filepath = r'C:\Users\krzys\Desktop\Języki Skryptowe LAB\lista1\lista2\zad1.py'          #Podajemy bezwględną ścieżkę dostępu do pliku   - I sposób podziału
    print(os.path.basename(filepath))              #Zwróci nazwę pliku
    print(os.path.dirname(filepath))                #Zwróci ścieżkę dostępu do katalogu, w którym plik się znajduje.
    print(os.path.exists(filepath))             #Sprawdza czy dana ścieżka istnieje


    #Informacje dotyczące istniejących plików .py

    os.path.getmtime(filepath)                   #Data ostatniej modyfikacji
    time.localtime(os.path.getmtime(filepath))

    os.path.getctime(filepath)                   #Data utworzenia
    time.localtime(os.path.getctime(filepath))

    os.path.getatime(filepath)                   #Data ostatniego dostępu
    time.localtime(os.path.getatime(filepath))


    os.path.getsize(filepath)                    #Rozmiar pliku - rozmiar zwracany w bajtach.

    os.path.isfile(filepath)                     #Sprawdza czy określona ścieżka identyfikuje plik (file) czy katalog (dir)
    os.path.isdir(filepath)


    # II sposób podziału

    os.path.split(filepath)                      #Dzieli ścieżkę bezwzględną do pliku na nazwę pliku oraz ścieżkę dostępu do katalogu, w którym plik się znajduje.
    os.path.split(filepath)[1]                   #A jeżeli chcesz wyciągnąć jego poszczególne elementy używamy indeksowania
    os.path.split(filepath)[0]

    os.path.splitdrive(filepath)                 #Możliwość zwrócenia samej nazwy dysku - analizuje przekazaną ścieżkę dostępu do pliku i zwróci.
    os.path.splitdrive(filepath)[0]             #Zwraca tuple (nazwa dysku: ścieżka dostępu do pliku)
    os.path.splitdrive(filepath)[1]



if __name__ == '__main__':
    catalog()