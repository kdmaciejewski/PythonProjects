import CovidInfo
import calendar
import Logger

class Controller:

    def __init__(self, path):
        self.__info = CovidInfo.CovidInfo(path)
        self.logger = Logger.Logger()

    def compute(self, filename, about, country, continent, toSum, year, month, day, fMonth, fDay, tMonth, tDay):
        res = 0
        self.logger.name = filename
        self.logger.write("option: " + str(about))

        if fMonth is None:
            if day is None:
                if month is None:
                    if continent is None:
                        return self.__info.for_country(about, country.capitalize(), toSum)
                    else:
                        return self.__info.for_continent(about, continent.capitalize(), toSum)
                else:
                    if continent is None:
                        return self.__info.for_range_country(about, year, month, 1, year, month,
                                                             calendar.monthrange(year, month)[1],
                                                             country.capitalize(), toSum)
                    else:
                        return self.__info.for_range_continent(about, year, month, 1, year, month,
                                                               calendar.monthrange(year, month)[1],
                                                               continent.capitalize(), toSum)
            else:
                if continent is None:
                    return self.__info.for_date_country(about, year, month, day, country.capitalize())
                else:
                    return self.__info.for_date_continent(about, year, month, day, continent.capitalize(), toSum)
        else:
            if continent is None:
                return self.__info.for_range_country(about, year, fMonth, fDay, year, tMonth, tDay,
                                                     country.capitalize(), toSum)
            else:
                return self.__info.for_range_continent(about, year, fMonth, fDay, year, tMonth, tDay,
                                                       continent.capitalize(), toSum)
