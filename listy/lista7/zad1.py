import pandas as pd
import time
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
all_cases = []
by_date = {}
by_country = {}
l1 = []

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            l1.append((te - ts) * 1000)
            print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))

        return result
    return timed


def create():
    # all_cases.append(('Polska', 2022, 4, 20, 21, 301))
    # all_cases.append(('Niemcy', 2022, 4, 20, 340, 198583))
    # all_cases.append(('Czechy', 2022, 4, 20, 25, 3596))
    with open('Covid.txt', 'r', encoding="utf-8") as file:
        for line in file:
            s = line.strip().split()
            all_cases.append((s[6], s[3], s[2], s[1], s[5], s[4]))

            if (s[3], s[2], s[1]) in by_date.keys():

                by_date[(s[3], s[2], s[1])].append((s[6], s[5], s[4]))
            else:
                by_date[(s[3], s[2], s[1])] = [(s[6], s[5], s[4])]

            if s[6] in by_country.keys():
                by_country[s[6]] = by_country[s[6]] + ((s[3], s[2], s[1], s[5], s[4]), )
            else:
                by_country[s[6]] = ((s[3], s[2], s[1], s[5], s[4]), )

    file.close()

# zadanie 2
@timeit
def for_date_a(year, month, day):

    zgony = 0
    przypadki = 0
    for i in all_cases:
        if int(i[1]) == year and int(i[2]) == month and int(i[3]) == day:
            zgony = zgony + int(i[4])
            przypadki = przypadki + int(i[5])

    print(f"Dzienna liczba zgonów: {zgony}")
    print(f"Dzienna liczba przypadków: {przypadki}")
    return (zgony, przypadki)

@timeit
def for_date_d(year, month, day):

    zgony = 0
    przypadki = 0

    l = by_date[(str(year), str(month), str(day))]
    for i in l:
        zgony = zgony + int(i[1])
        przypadki = przypadki + int(i[2])

    print(f"Dzienna liczba zgonów: {zgony}")
    print(f"Dzienna liczba przypadków: {przypadki}")

    return (zgony, przypadki)
@timeit
def for_date_c(year, month, day):
    zgony = 0
    przypadki = 0

    for key, value in by_country.items():
        for val in value:
            if int(val[0]) == year and int(val[1]) == month and int(val[2]) == day:
                zgony = zgony + int(val[3])
                przypadki = przypadki + int(val[4])

    print(f"Dzienna liczba zgonów: {zgony}")
    print(f"Dzienna liczba przypadków: {przypadki}")
    return (zgony, przypadki)
@timeit
def for_country_a(country):

    zgony = 0
    przypadki = 0

    for i in all_cases:
        if country == i[0]:
            zgony = zgony + int(i[4])
            przypadki = przypadki + int(i[5])

    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")

    return (zgony, przypadki)
@timeit
def for_country_d(country):

    zgony = 0
    przypadki = 0

    for key, value in by_date.items():
        for val in value:
            if val[0] == country:
                zgony = zgony + int(val[1])
                przypadki = przypadki + int(val[2])

    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")

    return (zgony, przypadki)
@timeit
def for_country_c(country):
    zgony = 0
    przypadki = 0

    l = by_country[country]
    for i in l:
        zgony = zgony + int(i[3])
        przypadki = przypadki + int(i[4])

    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")

    return (zgony, przypadki)

@timeit
def for_date_country_a(year, month, day, country):

    zgony = 0
    przypadki = 0

    for i in all_cases:
        if country == i[0] and int(i[1]) == year and int(i[2]) == month and int(i[3]) == day:
            zgony = zgony + int(i[4])
            przypadki = przypadki + int(i[5])

    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")

@timeit
def for_date_country_d(year, month, day, country):
    zgony = 0
    przypadki = 0

    l = by_date[(str(year), str(month), str(day))]
    for i in l:
        if i[0] == country:
            zgony = zgony + int(i[1])
            przypadki = przypadki + int(i[2])


    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")

@timeit
def for_date_country_c(year, month, day, country):

    zgony = 0
    przypadki = 0

    l = by_country[country]
    for i in l:
        if int(i[0]) == year and int(i[1]) == month and int(i[2]) == day:
            zgony = zgony + int(i[3])
            przypadki = przypadki + int(i[4])

    print(f"liczba zgonów: {zgony}")
    print(f"liczba przypadków: {przypadki}")



if __name__ == '__main__':
    create()
    print('\nzadanie 2')

    for_date_a(2020, 11, 24)
    for_date_d(2020, 11, 24)
    for_date_c(2020, 11, 24)

    data = {'1': l1[0], '2': l1[1], '3': l1[2]}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, values, color='blue',
            width=0.4)

    plt.xlabel("Metody")
    plt.ylabel("Czas[ms]")
    plt.title("Wykres zależności zadania 2")
    plt.show()



    print('\nzadanie 3')

    for_country_a('Poland')
    for_country_d('Poland')
    for_country_c('Poland')

    data = {'1': l1[3], '2': l1[4], '3': l1[5]}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, values, color='blue',
            width=0.4)

    plt.xlabel("Metody")
    plt.ylabel("Czas[ms]")
    plt.title("Wykres zależności zadania 3")
    plt.show()

    print('\nzadanie 4')
    for_date_country_a(2020, 11, 24, 'Poland')
    for_date_country_d(2020, 11, 24, 'Poland')
    for_date_country_c(2020, 11, 24, 'Poland')

    data = {'1': l1[6], '2': l1[7], '3': l1[8]}
    courses = list(data.keys())
    values = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    plt.bar(courses, values, color='blue',
            width=0.4)

    plt.xlabel("Metody")
    plt.ylabel("Czas[ms]")
    plt.title("Wykres zależności zadania 4")
    plt.show()
