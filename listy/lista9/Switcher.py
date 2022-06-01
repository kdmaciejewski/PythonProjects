import CovidData
import Logger
import calendar

class Switcher:
    def __init__(self, path):
        self.data = CovidData.CovidData(path)
        self.logger = Logger.Logger()

    def fit(self, filename, option, country, continent, day, month, year, begDay, begMonth, endDay, endMonth, sumowanie):
        res = 0
        self.logger.name = filename
        self.logger.write("option: " + str(option))
        
        if begMonth is None:
            if day is None:
                if month is None:
                    if continent is None:
                        if country is not None:
                            return self.data.show_country(option, country.capitalize(), sumowanie)
                    else:
                        return self.data.show_continent(option, continent.capitalize(), sumowanie)
                else:
                    if continent is None:
                        return self.data.show_country_range(option, 1,month, year,
                                                             calendar.monthrange(year, month)[1], month, year,
                                                             country.capitalize(), sumowanie)
                    else:
                        return self.data.show_continent_range(option, 1, month, year,
                                                              calendar.monthrange(year, month)[1], month, year,
                                                              continent.capitalize(), sumowanie)
            else:
                if continent is None:
                    return self.data.show_country_date(option, day, month, year, country.capitalize())
                else:
                    return self.data.show_continent_date(option, day, month, year, continent.capitalize(), sumowanie)
        else:
            if continent is None:
                return self.data.show_country_range(option, begDay, begMonth, year, endDay,endMonth, year,
                                                     country.capitalize(), sumowanie)
            else:
                return self.data.show_continent_range(option, begDay, begMonth, year, endDay,endMonth, year,
                                                       continent.capitalize(), sumowanie)
