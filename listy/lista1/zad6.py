def create(names, surnames, snames):
    print("Witaj!")

    name = input('Podaj imie: ')
    surname = input('Podaj nazwisko: ')
    print('{0:s} {1:s} dobrze, że jesteś z nami!'.format(name, surname))
    names.append(name)
    surnames.append(surname)
    snames.append((name, surname))
    print('Twój adres email to: {0:s}.{1:s}@pwr.edu.pl'.format(name.lower(), surname.lower()))


if __name__ == '__main__':
    names = []
    surnames = []
    snames = []
    create(names, surnames, snames)
    create(names, surnames, snames)
    print(names)
    print(surnames)
    print(snames)
