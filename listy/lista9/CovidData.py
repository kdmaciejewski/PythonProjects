import datetime

class CovidData:
    def __init__(self, path):

        cases = {}
        with open(path, encoding='utf-8') as file:
            lines = file.readlines()
            self.header = lines.pop(0)

            for line in lines:
                split = line.split()
                if len(split) >= 11:                                        # kluczen jest krotka państwo, kontynent
                    countryVal = cases.get(split[6]) or []                      #jeżeli są już wartości dla tego państwa
                    countryVal.append(                                          #data, zgony, przypadki, kontynent
                        (datetime.date(int(split[3]), int(split[2]), int(split[1])), split[5], split[4], split[10]))
                    cases.update({split[6]: countryVal})

        self.countries = cases


    def printCountries(self):
        print(self.countries.items())

    def show_country(self, option, country, sumowanie):        #option czy zgony czy przypadki
        result = []
        for i in self.countries[country]:
            if option == 'deaths':
                result.append((i[0], i[1]))
            else:
                result.append((i[0], i[2]))            # dodawanie przypadków

        if sumowanie:
            sum = 0
            for i in result:
                sum = sum + int(i[1])
            return sum
        return result

    def show_continent(self, option, continent, sumowanie):
        result = []

        for i in self.countries:
            if self.countries[i][0][3] == continent:
                for day in self.countries[i]:
                    if option == 'deaths':
                        result.append((i, day[0], day[1]))
                    else:
                        result.append((i, day[0], day[2]))

        if sumowanie:
            sum = 0
            for i in result:
                sum += int(i[2])
            return sum
        else:
            return result

    def show_country_date(self, option, day, month, year, country):
        d = datetime.date(year, month, day)

        for i in self.countries[country]:
            if i[0] == d:
                if option == 'deaths':
                    return i[1]
                else:
                    return i[2]


    def show_continent_date(self, option, day, month, year, continent, sumowanie):
        d = datetime.date(year, month, day)
        result = []
        for i in self.countries:
            if self.countries[i][0][3] == continent.capitalize():
                for day in self.countries[i]:
                    if d == day[0]:
                        if option == 'deaths':
                            result.append((i, day[1]))
                        else:
                            result.append((i, day[2]))
        if sumowanie:
            sum = 0
            for i in result:
                sum += int(i[1])
            return sum
        return result

    def show_country_range(self, option, BegDay, BegMonth, BegYear, EndDay, EndMonth, EndYear, country, sumowanie):
        beginning = datetime.date(BegYear, BegMonth, BegDay)
        end = datetime.date(EndYear, EndMonth, EndDay)
        result = []

        for i in self.countries[country]:
            if beginning <= i[0] <= end:
                if option == 'deaths':
                    result.append((i[0], i[1]))
                else:
                    result.append((i[0], i[2]))

        if sumowanie:
            sum = 0
            for i in result:
                sum += int(i[1])
            return sum
        return result

    def show_continent_range(self, option, BegDay, BegMonth, BegYear, EndDay, EndMonth, EndYear, continent, sumowanie):
        beginning = datetime.date(BegYear, BegMonth, BegDay)
        end = datetime.date(EndYear, EndMonth, EndDay)
        result = []

        for i in self.countries:
            if self.countries[i][0][3] == continent.capitalize():
                for day in self.countries[i]:
                    if beginning <= day[0] <= end:
                        if option == 'deaths':
                            result.append((day[0], day[1]))
                        else:
                            result.append((day[0], day[2]))
        if sumowanie:
            sum = 0
            for i in result:
                sum += int(i[1])
            return sum
        else:
            return result


if __name__ == '__main__':
    c = CovidData("Covid.txt")
    #c.printCountries()
    # print(c.show_country('deaths', 'Poland', True))
    # print(c.show_continent('deaths', "Asia", False))
    print(c.show_country_date('cases', 20, 11, 2020, "Austria"))
    # print(c.show_continent_date('cases', 20, 11, 2020, 'Africa', True))
    # print(c.show_country_range('cases', 20, 11, 2020, 20, 1, 2021, 'Austria', True))
    # print(c.show_continent_range('cases', 20, 11, 2020, 20, 1, 2021, 'Africa', True))












