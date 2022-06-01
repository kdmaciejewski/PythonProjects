import os

#zapis do pliku dwóch różnych danych

def save():
    s = 'AAAAAAAAAA'
    l = ['A', 'B', 'C']

    with open("C:\\Users\\krzys\\Desktop\\Języki Skryptowe LAB\\listy\\lista2\\zad7.txt", 'w') as file:  # Zapis do pliku
        file.write(s)
        file.write('\n')

        for i in l:
            file.write(i + '\n')

def website():
    s = input("Podaj ulubioną stronę internetową ")
    with open("C:\\Users\\krzys\\Desktop\\Języki Skryptowe LAB\\listy\\lista2\\zad7.txt",
              'w') as file:  # Zapis do pliku
        file.write(s)
        file.write('\n')

def website_dopisanie_odczytanie():
    s = input("Podaj ulubioną stronę internetową ")
    with open("C:\\Users\\krzys\\Desktop\\Języki Skryptowe LAB\\listy\\lista2\\zad7.txt",
              'a+') as file:  # Zapis do pliku
        file.write(s)
        file.write('\n')

        file.seek(0)  # file pointer at end, move to beginning

        print(file.read())


def open_file():
    with open("C:\\Users\\krzys\\Desktop\\Języki Skryptowe LAB\\listy\\lista2\\zad7.txt", 'r') as file:
        for line in file:
            print(line, end='')


if __name__ == '__main__':
    save()
    open_file()
    website_dopisanie_odczytanie()
    website()
    open_file()

