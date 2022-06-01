import datetime
import time


class CovidInfo:

    def __init__(self, path):
        cases = {}

        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            self.header = lines.pop(0)

            for line in lines:
                split = line.split()
                if len(split) >= 11:
                    tmpCountrVal = cases.get(split[6]) or []
                    tmpCountrVal.append(
                        (datetime.date(int(split[3]), int(split[2]), int(split[1])), split[5], split[4], split[10]))
                    cases.update({split[6]: tmpCountrVal})

        self.by_country = cases

    def printItems(self):
        print(self.by_country.items())

    def for_country(self, about, country, sum):
        everyday = []
        for elem in self.by_country[country]:
            if about.lower() == "cases":
                everyday.append((elem[0], elem[2]))
            else:
                everyday.append((elem[0], elem[1]))
        if sum:
            tmp = 0
            for elem in everyday:
                tmp += int(elem[1])
            return tmp
        else:
            return everyday

    def for_continent(self, about, continent, sum):
        everyday = []

        for country in self.by_country:
            if self.by_country[country][0][3] == continent:
                for day in self.by_country[country]:
                    if about.lower() == "deaths":
                        everyday.append((country, day[0], day[1]))
                    else:
                        everyday.append((country, day[0], day[2]))
        if sum:
            tmp = 0
            for elem in everyday:
                tmp += int(elem[2])
            return tmp
        else:
            return everyday

    def for_date_country(self, about, year, month, day, country):
        date = datetime.date(year, month, day)
        tak = self.by_country[country]
        for elem in tak:
            if elem[0] == date:
                if about == "deaths":
                    return elem[1]
                else:
                    return elem[2]

    def for_date_continent(self, about, year, month, day, continent, sum):
        thatday = []
        date = datetime.date(year, month, day)
        for country in self.by_country:
            if self.by_country[country][0][3] == continent:
                for day in self.by_country[country]:
                    if date == day[0]:
                        if about.lower() == "deaths":
                            thatday.append((country, day[1]))
                        else:
                            thatday.append((country, day[2]))
        if sum:
            tmp = 0
            for elem in thatday:
                tmp += int(elem[1])
            return tmp
        else:
            return thatday


    def for_range_country(self, about, fYear, fMonth, fDay, tYear, tMonth, tDay, country, sum):
        fDate = datetime.date(fYear, fMonth, fDay)
        tDate = datetime.date(tYear, tMonth, tDay)
        inRange = []
        for elem in self.by_country[country]:
            if fDate <= elem[0] <= tDate:
                if about == "deaths":
                    inRange.append((elem[0], elem[1]))
                else:
                    inRange.append((elem[0], elem[2]))
        if sum:
            tmp = 0
            for elem in inRange:
                tmp += int(elem[1])
            return tmp
        else:
            return inRange

    def for_range_continent(self, about, fYear, fMonth, fDay, tYear, tMonth, tDay, continent, sum):
        fDate = datetime.date(fYear, fMonth, fDay)
        tDate = datetime.date(tYear, tMonth, tDay)
        inRange = []
        for country in self.by_country:
            for day in self.by_country[country]:
                if self.by_country[country][0][3] == continent:
                    for day in self.by_country[country]:
                        if fDate <= day[0] <= tDate:
                            if about.lower() == "deaths":
                                inRange.append((country, day[0], day[1]))
                            else:
                                inRange.append((country, day[0], day[2]))
        if sum:
            tmp = 0
            for elem in inRange:
                tmp += int(elem[2])
            return tmp
        else:
            return inRange


# class Log:
#
#     def __init__(self, path):
#         self.path = path
#
#     def write(self, message):
#         text = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + " " + message + "\n"
#         with open(self.path, "a") as file:
#             file.write(text)


def test():
    a = "a"
    print(a == "a")
    diction = {}
    lista = [('a', 1), ('a', 2), ('a', 3), ('a', 11), ('b', 2), ('c', 3), ('b', 4)]
    for elem in lista:
        tmp = diction.get(elem[0]) or []
        tmp.append(elem[1])
        diction.update({elem[0]: tmp})

    print(lista)
    print(diction)


def main():
    c = CovidInfo("../szym/Covid.txt")
    print(c.for_continent("deaths", "Asia", True))
    # print(c.for_country("deaths", "France", True))
    # print(c.for_range_continent("cases", 2020, 2, 1, 2020, 2, 1, "Asia", True))
    # print(c.for_range_country("cases", 2020, 1, 11, 2020, 2, 29, "Albania", True))
    # print(c.for_date_continent("cases", 2020, 11, 1, "Asia", True))
    # print(c.for_date_country("cases", 2020, 3, 11, "Albania"))


if __name__ == '__main__':
    main()
