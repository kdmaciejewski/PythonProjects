import sys
import Switcher
import calendar
import Logger

months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
          "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}


class Cons:
    continents = ["asia", "europe", "africa", "america", "oceania"]

    def __init__(self, switcher: Switcher, logger: Logger):
        self.year = 2020
        self.option = 'deaths'
        self.day = None
        self.month = None
        self.begDay = None
        self.begMonth = None
        self.endDay = None
        self.endMonth = None
        self.country = "Austria"
        self.continent = None
        self.sumowanie = False
        self.switcher = switcher
        self.logger = logger

    def runSwitcher(self):
        res = self.switcher.fit("Covid.txt", self.option, self.country,
                                self.continent, self.day, self.month, self.year, self.begDay,
                                self.begMonth, self.endDay, self.endMonth, self.sumowanie)

        answer = ""
        if self.sumowanie:
            answer = answer + str(res)
        else:
            #answer = answer + "\n"
            count = 0
            for line in res:
                # if count == 60:
                #     break
                for elem in line:
                    answer = answer + str(elem) + " "
                # answer += str(line)
                #answer = answer + "\n"
                answer = answer + "| "
                count += 1
        #print(res)
        print(answer)

    def start(self):
        print("Write command:")

        while True:
            zdanie = sys.stdin.readline()
            words = zdanie.split()
            # for word in sys.stdin.readline().split():
            #     words.append(word)
            # print(zdanie)
            # print(words)
            showCases = words[0] + " " + words[1]


            if 'Exit' == words[0]:
                break
            elif 'Show res' == showCases:
                self.switcher.logger.write("option: " + str(self.option))   #zapisanie logów
                self.runSwitcher()                              #uruchomienie switchera
            elif 'Save to' == showCases:
                self.switcher.logger.name = words[2] if words[2] == "logs.txt" else "logs.txt"
            elif 'Set total' == showCases:
                if words[2] == 'on':
                    self.sumowanie = True
                elif words[2] == 'off':
                    self.sumowanie = False
                else:
                    raise ValueError('Wrong on/off value')

            elif "Show" == words[0]:
                self.showHelper(words)

        print('End of program')

    def showHelper(self, words):

        if len(words) == 2:  # Show cases/deaths, jeśli wcześniej nie podano kraju to domyślny
            if words[1] == 'deaths':
                if self.begDay != None and self.begMonth != None and self.endDay != None and self.endMonth != None:
                    self.option = 'deaths'
            elif words[1] == 'cases':
                if self.begDay != None and self.begMonth != None and self.endDay != None and self.endMonth != None:
                    self.option = 'cases'
            else:
                raise ValueError("Wrong command: Show cases/deaths")

        else:
            # Show from May 10 till June 20
            if words[1] == 'from':  # 3 RODZAJ
                if self.country != None or self.continent != None:
                    self.begDay = int(words[3]) if words[3].isdecimal() else None
                    self.begMonth = int(months[words[2].lower()]) if words[2].lower() in months else None
                    self.endDay = int(words[6]) if words[6].isdecimal() else None
                    self.endMonth = int(months[words[5].lower()]) if words[5].lower() in months else None

                    if self.begDay == None or self.begMonth == None or self.endMonth == None or self.endDay == None:
                        raise ValueError('Wrong beg or end')

            elif words[1] == 'deaths':
                self.option = 'deaths'
                if words[2] == "in":
                    continents = ["asia", "europe", "africa", "america", "oceania"]
                    if (words[3].lower() in continents):
                        self.continent = words[3].capitalize()
                        self.country = None

                        if words[4] == 'in':
                            self.inHelper(words)
                        if words[4] == 'on':
                            self.onHelper(words)
                        if words[4] == 'from':
                            self.inHelper(words)
                    else:
                        self.country = words[3].capitalize()
                        self.continent = None
                        if words[4] == 'in':
                            self.inHelper(words)
                        if words[4] == 'on':
                            self.onHelper(words)
                        if words[4] == 'from':
                            self.fromHelper(words)
                else:
                    raise ValueError("Missing 'in'/'on'/'from' word")
            elif words[1] == 'cases':
                self.option = 'cases'
                if words[2] == "in":
                    continents = ["asia", "europe", "africa", "america", "oceania"]
                    if (words[3].lower() in continents):
                        self.continent = words[3].capitalize()
                        self.country = None
                        if words[4] == 'in':
                            self.inHelper(words)
                        if words[4] == 'on':
                            self.onHelper(words)
                        if words[4] == 'from':
                            self.inHelper(words)
                    else:
                        self.country = words[3].capitalize()
                        self.continent = None
                        if words[4] == 'in':
                            self.inHelper(words)
                        if words[4] == 'on':
                            self.onHelper(words)
                        if words[4] == 'from':
                            self.fromHelper(words)
                else:
                    raise ValueError("Missing 'in'/'on'/'from' word")
            else:
                raise ValueError("Wrong show command")

    def inHelper(self, words):
        if (words[5].lower() in months):
            self.month = months[words[5].lower()]
            self.begDay = None
            self.begMonth = None
            self.endDay = None
            self.endMonth = None
        else:
            raise ValueError("Wrong name of month")

    def onHelper(self, words):
        if (words[5].lower() in months):
            self.month = months[words[5].lower()]
            if words[6].isdecimal():
                if 0 < int(words[6]) <= calendar.monthrange(self.year, months[words[5].lower()])[1]:
                    self.day = int(words[6])
                    self.begDay = None
                    self.begMonth= None
                    self.endDay= None
                    self.endMonth= None
                else:
                    raise ValueError('Wrong numebr of days for that month')
            else:
                raise ValueError("Not decimal number of day")
        else:
            raise ValueError("Wrong name of month")

    def fromHelper(self, words):
        if words[4] == 'from' and words[7] == 'till':
            if (words[5].lower() in months) and (words[8].lower() in months):
                self.begMonth = months[words[5].lower()]
                self.endMonth = months[words[8].lower()]
                if words[6].isdecimal() and words[9].isdecimal():
                    if (0 < int(words[6]) <= calendar.monthrange(self.year, months[words[5].lower()])[1]
                            and 0 < int(words[9]) <= calendar.monthrange(self.year, months[words[8].lower()])[1]):
                        self.begDay = int(words[6])
                        self.endDay = int(words[9])
                        self.day = None
                        self.month = None
                    else:
                        raise ValueError('Wrong numebr of days for a month')
                else:
                    raise ValueError("Not decimal number of day")
            else:
                raise ValueError("Wrong name of month")
        else:
            raise ValueError('Wrong from/till expression')


#   Set total on | off                      # sumowanie lub nie wybranych wierszy

# 1 RODZAJ

#   Show deaths in Asia in April        6
#   Show cases in Poland in June

# 2 RODZAJ
#   Show deaths in Asia on April 10     7
#   Show cases in Poland on June 10
# 2.5 RODZAJ
#   Show deaths in Asia from May 10 till June 20        10
#   Show cases in Poland from May 10 till June 20

# 3 RODZAJ
#   Show from May 10 till June 20       7

# domyślnie przyjmujemy poprzednio użyte cases/deaths oraz zakres terytorialny
#
#   Show cases  # j.w. ale dla przypadków
#   Show deaths

#   Exit

if __name__ == '__main__':
    console = Cons(Switcher.Switcher("Covid.txt"), Logger.Logger())
    console.start()

    # for line in sys.stdin:
    #     if 'q' == line.rstrip():
    #         break
    #     print(f'Input : {line}')
    #
    # print("Exit")
