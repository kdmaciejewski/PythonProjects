from tkinter import *
import tkinter.messagebox
from tkinter import messagebox
import Switcher
from datetime import datetime


def createMenu(switcher: Switcher):

    months = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
              "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}

    year = 2020

    w = Tk()

    w.title("Informacje o Covid-19")
    w.geometry('380x300')

    f2 = Frame(w)
    f2.grid(column=1, row=1)

    option = StringVar(value='deaths')

    l1 = Label(w, text="Type: ")
    l1.grid(column=0, row=1)

    def elo():
        print(option.get())
    
    casdeaths = Radiobutton(f2, text="deaths", value="deaths", variable=option)
    casdeaths.grid(column=0, row=0)
    casdeaths = Radiobutton(f2, text="cases", value="cases", variable=option)
    casdeaths.grid(column=1, row=0)

    l3 = Label(w, text="Country: ")
    l3.grid(column=0, row=2)
    country = Entry(w, width=30)
    country.grid(column=1, row=2)

    l4 = Label(w, text="Continent: ")
    l4.grid(column=0, row=3)
    continent = Entry(w, width=30)
    continent.grid(column=1, row=3)

    l5 = Label(w, text="Month: (January - December)")
    l5.grid(column=0, row=4)
    month = Entry(w, width=30)
    month.grid(column=1, row=4)

    l6 = Label(w, text="Day: ")
    l6.grid(column=0, row=5)
    day = Entry(w, width=30)
    day.grid(column=1, row=5)

    l7 = Label(w, text="Beginning day: ")
    l7.grid(column=0, row=7)
    begDay = Entry(w, width=30)
    begDay.grid(column=1, row=7)

    l8 = Label(w, text="Beginning month: ")
    l8.grid(column=0, row=6)
    begMonth = Entry(w, width=30)
    begMonth.grid(column=1, row=6)

    l9 = Label(w, text="End day: ")
    l9.grid(column=0, row=9)
    endDay = Entry(w, width=30)
    endDay.grid(column=1, row=9)

    l10 = Label(w, text="End month: ")
    l10.grid(column=0, row=8)
    endMonth = Entry(w, width=30)
    endMonth.grid(column=1, row=8)

    frame = Frame(w)
    frame.grid(column=1, row=10)

    sumowanie = BooleanVar()

    l11 = Label(w, text="Sumowanie: ")
    l11.grid(column=0, row=10)

    sumowanieOn = Radiobutton(frame, text="on", value=True, variable=sumowanie)
    sumowanieOn.grid(column=0, row=0)
    sumowanieOn = Radiobutton(frame, text="off", value=False, variable=sumowanie)
    sumowanieOn.grid(column=1, row=0)

    l12 = Label(w, text="File name for logs: ")
    l12.grid(column=0, row=11)
    fileName = Entry(w, width=30)
    fileName.grid(column=1, row=11)

    def results():
        answer = ""
        if option.get() != "deaths" and option.get() != "cases":
            userOption = "cases"
        else:
            userOption = option.get()

        userCountry = country.get().capitalize() if country.get() != "" else None
        userContinent = continent.get().capitalize() if continent.get() != "" else None
        userMonth = months[month.get().lower()] if month.get() != "" else None
        userDay = int(day.get()) if day.get != "" and day.get().isalnum() else None
        userBegDay = int(begDay.get()) if begDay.get != "" and begDay.get().isalnum() else None
        userBegMonth = months[begMonth.get().lower()] if begMonth.get() != "" else None
        userEndMonth = months[endMonth.get().lower()] if endMonth.get() != "" else None
        userEndDay = int(endDay.get()) if endDay.get != "" and endDay.get().isalnum() else None
        userFileName = fileName.get() if fileName.get() != None else "logfiles.txt"

        res = switcher.fit(userFileName, userOption, userCountry, userContinent, userDay, userMonth, year,
                               userBegDay, userBegMonth, userEndDay, userEndMonth, sumowanie.get())

        # userOption = "cases"
        # userCountry = None
        # userContinent = "Asia"
        # userMonth = None
        # userDay = None
        # userBegDay = None
        # userBegMonth = None
        # userEndMonth = None
        # userEndDay = None
        # userFileName = "logfiles.txt"
        # year = 2020
        # s = Switcher.Switcher("Covid.txt")
        # res = switcher.fit(userFileName, userOption, userCountry, userContinent, userDay, userMonth, year,
        #                    userBegDay, userBegMonth, userEndDay, userEndMonth, True)

        #print(res)


        if userBegMonth is None:
            if userDay is None:
                if userMonth is None:
                    if userContinent is None:
                        answer = ("%s caused by Covid-19 in %s: " % (userOption.capitalize(), userCountry.capitalize()))
                    else:
                        answer = ("%s caused by Covid-19 in %s: " % (userOption.capitalize(), userContinent.capitalize()))
                else:
                    tmpmonth = datetime.strptime(str(userMonth), "%m")
                    if userContinent is None:
                        answer = ("%s caused by Covid-19 in %s in %s: " % (userOption.capitalize(), userCountry.capitalize(),
                                                                            tmpmonth.strftime("%B")))
                    else:
                        answer = ("%s caused by Covid-19 in %s in %s: " % (userOption.capitalize(), userContinent.capitalize(),
                                                                            tmpmonth.strftime("%B")))
            else:
                tmpmonth = datetime.strptime(str(userMonth), "%m")
                if userContinent is None:
                    answer = ("%s caused by Covid-19 in %s on %s %d: " % (
                        userOption.capitalize(), userCountry.capitalize(), tmpmonth.strftime("%B"), userDay))
                else:
                    answer = ("%s caused by Covid-19 in %s on %s %d: " % (userOption.capitalize(), userContinent.capitalize(),
                                                                           tmpmonth.strftime("%B"), userDay))
        else:
            tmpbegMonth = datetime.strptime(str(userBegMonth), "%m")
            tmpendMonth = datetime.strptime(str(userEndMonth), "%m")
            if userContinent is None:
                answer = ("%s caused by Covid-19 in %s from %s %d till %s %d: " % (
                    userOption.capitalize(), userCountry.capitalize(), tmpbegMonth.strftime("%B"), userBegDay, tmpendMonth.strftime("%B"),
                    userEndDay))
            else:
                answer = ("%s caused by Covid-19 in %s from %s %d till %s %d: " % (
                    userOption.capitalize(), userContinent.capitalize(), tmpbegMonth.strftime("%B"), userBegDay,
                    tmpendMonth.strftime("%B"), userEndDay))

        if sumowanie.get():
            answer = answer + str(res)
        else:
            answer = answer + "\n"
            count = 0
            for line in res:
                if count == 60:
                    break
                for elem in line:
                    answer = answer + str(elem) + " "
                # answer += str(line)
                answer = answer + "\n"
                count += 1

        messagebox.showinfo("Results", message=answer)

    b = Button(w, text="Show", command=results)
    b.grid(column=1, row=12)

    w.mainloop()



if __name__ == '__main__':
    s = Switcher.Switcher("Covid.txt")
    createMenu(s)
    # userOption = "cases"
    # userCountry = None
    # userContinent = "Asia"
    # userMonth = None
    # userDay = None
    # userBegDay = None
    # userBegMonth = None
    # userEndMonth = None
    # userEndDay = None
    # userFileName = "logfiles.txt"
    # year = 2020
    # s = Switcher.Switcher("Covid.txt")
    # res = s.fit(userFileName, userOption, userCountry, userContinent, userDay, userMonth, year,
    #                    userBegDay, userBegMonth, userEndDay, userEndMonth, False)
    #
    # print(res)
