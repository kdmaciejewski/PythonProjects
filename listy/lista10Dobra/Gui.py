import tkinter
from tkinter import *
import tkinter.messagebox
import Controller
from datetime import datetime
import configparser
import tkinter as tk
from tkinter.constants import NSEW
import os
from PIL import ImageTk, Image

class Gui(tkinter.Frame):
    months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7,
              'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

    config = "config.txt"

    def __init__(self, controller: Controller, master=None):
        #odczytanie pliku konfiguracyjnego
        self.config = configparser.ConfigParser()
        self.config.read(Gui.config, "UTF8")
        default = self.config["DEFAULT"]
        self.vYear = 2020
        self.vAbout = default.get('about', 'deaths')
        self.vCountry = default.get('country', 'Afghanistan')
        self.vtoSum = True
        self.vContinent = default.get('continent', 'Europe')
        self.vMonth = None
        self.vDay = None
        self.vfMonth = None
        self.vfDay = None
        self.vtMonth = None
        self.vtDay = None
        self.logger = 'logfiles.txt'
        self.controller = controller
        tkinter.Frame.__init__(self, master)
        self.parent = master
        self.parent.title("Covid-19 App")
        self.parent.protocol("WM_DELETE_WINDOW", self.fileQuit)

        self.geometry = default.get('bazowa_geometria', "900x600")
        self.parent.geometry(self.geometry)
        self.createTaskBar()
        self.createWindowCountry()
        self.createResultWindow()
        self.createStatusBar()
        self.createMenu()
        self.parent.columnconfigure(0, pad=15)
        self.parent.columnconfigure(1, weight=4000)
        self.parent.columnconfigure(2, weight=100)
        self.parent.rowconfigure(0, weight=1)
        self.parent.rowconfigure(1, weight=9999)
        self.parent.rowconfigure(2, weight=1)

    def show(self):
        self.result.delete(0, END)  # czyścimy pole wynikowe

        try:

            res = self.controller.compute(self.logger, self.vAbout, self.vCountry, self.vContinent, self.vtoSum,
                                      self.vYear,self.vMonth,self.vDay, self.vfMonth, self.vfDay, self.vtMonth,
                                      self.vtDay)
            if self.vfMonth is None:
                if self.vDay is None:
                    if self.vMonth is None:
                        if self.vContinent is None:
                            answer = ("All %s due to Covid-19 in %s: " % (self.vAbout, self.vCountry.capitalize()))
                        else:
                            answer = ("All %s due to Covid-19 in %s: " % (self.vAbout, self.vContinent.capitalize()))
                    else:
                        tmpmonth = datetime.strptime(str(self.vMonth), "%m")
                        if self.vContinent is None:
                            answer = ("All %s due to Covid-19 in %s in %s: " % (self.vAbout, self.vCountry.capitalize(),
                                                                                tmpmonth.strftime("%B")))
                        else:
                            answer = ("All %s due to Covid-19 in %s in %s: " % (
                                self.vAbout, self.vContinent.capitalize(),
                                tmpmonth.strftime("%B")))
                else:
                    tmpmonth = datetime.strptime(str(self.vMonth), "%m")
                    if self.vContinent is None:
                        answer = ("All %s due to Covid-19 in %s on %s %d: " % (
                            self.vAbout, self.vCountry.capitalize(), tmpmonth.strftime("%B"), self.vDay))
                    else:
                        answer = ("All %s due to Covid-19 in %s on %s %d: " % (
                            self.vAbout, self.vContinent.capitalize(),
                            tmpmonth.strftime("%B"), self.vDay))
            else:
                tmpfMonth = datetime.strptime(str(self.vfMonth), "%m")
                tmptMonth = datetime.strptime(str(self.vtMonth), "%m")
                if self.vContinent is None:
                    answer = ("All %s due to Covid-19 in %s from %s %d till %s %d: " % (
                        self.vAbout, self.vCountry.capitalize(), tmpfMonth.strftime("%B"), self.vfDay,
                        tmptMonth.strftime("%B"),
                        self.vtDay))
                else:
                    answer = ("All %s due to Covid-19 in %s from %s %d till %s %d: " % (
                        self.vAbout, self.vContinent.capitalize(), tmpfMonth.strftime("%B"), self.vfDay,
                        tmptMonth.strftime("%B"), self.vtDay))
            if self.vtoSum:
                self.result.insert(tkinter.END, answer)
                self.result.insert(tkinter.END, res)
            else:
                self.result.insert(tkinter.END, answer)
                for line in res:
                    tmp = ""
                    for elem in line:
                        tmp = tmp + str(elem) + " "
                    self.result.insert(tkinter.END, tmp)
            self.set_status_bar(answer)
        except ValueError:
            tkinter.messagebox.showinfo("Error", "Day number out of month range")

    def fileQuit(self, event=None):
        self.config["DEFAULT"]["bazowa_geometria"] = self.parent.winfo_geometry()
        with open(Gui.config, 'w') as file:
            if self.vCountry is not None:
                self.config.set('DEFAULT', 'country', str(self.vCountry))
            if self.vContinent is not None:
                self.config.set(section='DEFAULT', option='continent', value=str(self.vContinent))
            self.config.write(file)
        self.parent.destroy()

    def createWindowPoland(self):
        self.vAbout = 'cases'
        self.vCountry = 'Poland'
        self.vContinent = None
        self.vtoSum = False
        self.vMonth = None
        self.vDay = None
        self.vfMonth = None
        self.vfDay = None
        self.vtMonth = None
        self.vtDay = None
        self.show()

    def createWindowGermany(self):
        self.vAbout = 'cases'
        self.vCountry = 'Germany'
        self.vContinent = None
        self.vtoSum = False
        self.vMonth = None
        self.vDay = None
        self.vfMonth = None
        self.vfDay = None
        self.vtMonth = None
        self.vtDay = None
        self.show()

    def createWindowEu(self):
        self.vAbout = 'cases'
        self.vCountry = None
        self.vContinent = 'Europe'
        self.vtoSum = False
        self.vMonth = None
        self.vDay = None
        self.vfMonth = None
        self.vfDay = None
        self.vtMonth = None
        self.vtDay = None
        self.show()

    def createWindowUSA(self):
        self.vAbout = 'cases'
        self.vCountry = None
        self.vContinent = "America"
        self.vtoSum = False
        self.vMonth = None
        self.vDay = None
        self.vfMonth = None
        self.vfDay = None
        self.vtMonth = None
        self.vtDay = None
        self.show()

    def createWindowCountry(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label3 = Label(self.window, text="Country: ")
        label3.grid(column=0, row=0)
        country = Entry(self.window, width=30)
        country.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=4)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=4)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vCountry = country.get().lower().capitalize() if country.get() != "" else self.vCountry
            if self.vCountry is not None:
                self.vContinent = None
            self.vtoSum = toSum.get()
            self.vMonth = None
            self.vDay = None
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=5)

    def createWindowContinent(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label3 = Label(self.window, text="Continent: ")
        label3.grid(column=0, row=0)
        continent = Entry(self.window, width=30)
        continent.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=3)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=3)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vContinent = continent.get().lower().capitalize() if continent.get() != "" else self.vContinent
            if self.vContinent is not None:
                self.vCountry = None
            self.vtoSum = toSum.get()
            self.vContinent = continent.get().lower().capitalize() if continent.get() != "" else self.vContinent
            self.vMonth = None
            self.vDay = None
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None

            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=4)

    def createWindowCountryDate(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label2 = Label(self.window, text="Country: ")
        label2.grid(column=0, row=0)
        country = Entry(self.window, width=30)
        country.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        # toSum = BooleanVar()
        # label11 = Label(self.window, text="Sum: ")
        # label11.grid(column=0, row=2)
        # sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        # sumRadioOn.grid(column=0, row=0)
        # sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        # sumRadioOn.grid(column=1, row=0)

        label4 = Label(self.window, text="Day: ")
        label4.grid(column=0, row=2)
        day = Entry(self.window, width=30)
        day.grid(column=1, row=2)

        label3 = Label(self.window, text="Month: ")
        label3.grid(column=0, row=3)
        month = Entry(self.window, width=30)
        month.grid(column=1, row=3)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=4)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=4)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vCountry = country.get().lower().capitalize() if country.get() != "" else self.vCountry
            if self.vCountry is not None:
                self.vContinent = None
            self.vtoSum = True
            try:
                self.vMonth = Gui.months[month.get().lower()]
                self.vDay = int(day.get())
            except KeyError:
                tkinter.messagebox.showinfo("Error", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                     "April, May, June, July, August,\nSeptember, October, November,"
                                                     " December")
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Day number must be a number")
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=6)

    def createWindowContinentDate(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label2 = Label(self.window, text="Continent: ")
        label2.grid(column=0, row=0)
        continent = Entry(self.window, width=30)
        continent.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label4 = Label(self.window, text="Day: ")
        label4.grid(column=0, row=3)
        day = Entry(self.window, width=30)
        day.grid(column=1, row=3)

        label3 = Label(self.window, text="Month: ")
        label3.grid(column=0, row=4)
        month = Entry(self.window, width=30)
        month.grid(column=1, row=4)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=5)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=5)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vtoSum = toSum.get()
            self.vContinent = continent.get().lower().capitalize() if continent.get() != "" else self.vContinent
            if self.vContinent is not None:
                self.vCountry = None
            try:
                self.vMonth = Gui.months[month.get().lower()]
                self.vDay = int(day.get())
            except KeyError:
                tkinter.messagebox.showinfo("Result", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                      "April, May, June,July, August,\nSeptember, October, November, December")
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Day number must be a number")
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=6)

    def createWindowContinentMonth(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label3 = Label(self.window, text="Continent: ")
        label3.grid(column=0, row=0)
        continent = Entry(self.window, width=30)
        continent.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label2 = Label(self.window, text="Month: ")
        label2.grid(column=0, row=3)
        month = Entry(self.window, width=30)
        month.grid(column=1, row=3)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=4)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=4)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vtoSum = toSum.get()
            self.vContinent = continent.get().lower().capitalize() if continent.get() != "" else self.vContinent
            if self.vContinent is not None:
                self.vCountry = None
            try:
                self.vMonth = Gui.months[month.get().lower()]
            except KeyError:
                tkinter.messagebox.showinfo("Result", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                      "April, May, June,July, August,\nSeptember, October, November, December")
            self.vDay = None
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=5)

    def createWindowCountryMonth(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label3 = Label(self.window, text="Country: ")
        label3.grid(column=0, row=0)
        country = Entry(self.window, width=30)
        country.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label2 = Label(self.window, text="Month: ")
        label2.grid(column=0, row=3)
        month = Entry(self.window, width=30)
        month.grid(column=1, row=3)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=4)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=4)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vCountry = country.get().lower().capitalize() if country.get() != "" else self.vCountry
            if self.vCountry is not None:
                self.vContinent = None
            self.vtoSum = toSum.get()
            try:
                self.vMonth = Gui.months[month.get().lower()]
            except KeyError:
                tkinter.messagebox.showinfo("Result", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                      "April, May, June,July, August,\nSeptember, October, November, December")
            self.vDay = None
            self.vfMonth = None
            self.vfDay = None
            self.vtMonth = None
            self.vtDay = None
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=5)

    def createWindowCountryPeriod(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label2 = Label(self.window, text="Country: ")
        label2.grid(column=0, row=0)
        country = Entry(self.window, width=30)
        country.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label4 = Label(self.window, text="From day: ")
        label4.grid(column=0, row=3)
        fDay = Entry(self.window, width=30)
        fDay.grid(column=1, row=3)

        label3 = Label(self.window, text="From month: ")
        label3.grid(column=0, row=4)
        fMonth = Entry(self.window, width=30)
        fMonth.grid(column=1, row=4)

        label5 = Label(self.window, text="Till day: ")
        label5.grid(column=0, row=5)
        tDay = Entry(self.window, width=30)
        tDay.grid(column=1, row=5)

        label6 = Label(self.window, text="Till month: ")
        label6.grid(column=0, row=6)
        tMonth = Entry(self.window, width=30)
        tMonth.grid(column=1, row=6)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=7)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=7)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vCountry = country.get().lower().capitalize() if country.get() != "" else self.vCountry
            if self.vCountry is not None:
                self.vContinent = None
            self.vtoSum = toSum.get()
            self.vMonth = None
            self.vDay = None
            try:
                self.vfMonth = Gui.months[fMonth.get().lower()]
                self.vfDay = int(fDay.get())
                self.vtMonth = Gui.months[tMonth.get().lower()]
                self.vtDay = int(tDay.get())
            except KeyError:
                tkinter.messagebox.showinfo("Result", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                      "April, May, June,July, August,\nSeptember, October, November, December")
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Day number must be a number")
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=8)

    def createWindowContinentPeriod(self):
        self.window = tk.Frame(self.parent)
        self.window.grid(row=1, column=0, columnspan=1, rowspan=1, sticky=NSEW)

        label2 = Label(self.window, text="Continent: ")
        label2.grid(column=0, row=0)
        country = Entry(self.window, width=30)
        country.grid(column=1, row=0)

        frame = Frame(self.window)
        frame.grid(column=1, row=1)

        about = StringVar(value="deaths")
        label1 = Label(self.window, text="Deaths/Cases: ")
        label1.grid(column=0, row=1)
        aboutRadioOn = Radiobutton(frame, text="Deaths", value="deaths", variable=about)
        aboutRadioOn.grid(column=0, row=0)
        aboutRadioOn = Radiobutton(frame, text="Cases", value="cases", variable=about)
        aboutRadioOn.grid(column=1, row=0)

        frame1 = Frame(self.window)
        frame1.grid(column=1, row=2)

        toSum = BooleanVar()
        label11 = Label(self.window, text="Sum: ")
        label11.grid(column=0, row=2)
        sumRadioOn = Radiobutton(frame1, text="on", value=True, variable=toSum)
        sumRadioOn.grid(column=0, row=0)
        sumRadioOn = Radiobutton(frame1, text="off", value=False, variable=toSum)
        sumRadioOn.grid(column=1, row=0)

        label4 = Label(self.window, text="From day: ")
        label4.grid(column=0, row=3)
        fDay = Entry(self.window, width=30)
        fDay.grid(column=1, row=3)

        label3 = Label(self.window, text="From month: ")
        label3.grid(column=0, row=4)
        fMonth = Entry(self.window, width=30)
        fMonth.grid(column=1, row=4)

        label5 = Label(self.window, text="Till day: ")
        label5.grid(column=0, row=5)
        tDay = Entry(self.window, width=30)
        tDay.grid(column=1, row=5)

        label6 = Label(self.window, text="Till month: ")
        label6.grid(column=0, row=6)
        tMonth = Entry(self.window, width=30)
        tMonth.grid(column=1, row=6)

        label30 = Label(self.window, text="Save logs to: ")
        label30.grid(column=0, row=7)
        logname = Entry(self.window, width=30)
        logname.grid(column=1, row=7)
        self.logger = logname.get()

        def upgrade():
            self.vAbout = about.get()
            self.vtoSum = toSum.get()
            self.vContinent = country.get().lower().capitalize() if country.get() != "" else self.vContinent
            if self.vContinent is not None:
                self.vCountry = None
            self.vMonth = None
            self.vDay = None
            try:
                self.vfMonth = Gui.months[fMonth.get().lower()]
                self.vfDay = int(fDay.get())
                self.vtMonth = Gui.months[tMonth.get().lower()]
                self.vtDay = int(tDay.get())
            except KeyError:
                tkinter.messagebox.showinfo("Result", "Wrong month!\nAcceptable months: January, February,\nMarch, "
                                                      "April, May, June,July, August,\nSeptember, October, November, December")
            except ValueError:
                tkinter.messagebox.showinfo("Error", "Day number must be a number")
            self.show()

        button = Button(self.window, text="Show", command=upgrade)
        button.grid(column=1, row=8)

    def createResultWindow(self):
        self.result = tk.Listbox(self.parent)
        self.result.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=NSEW)

    def about(self):
        self.result = tk.Listbox(self.parent)
        self.result.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=NSEW)
        self.result.insert(tkinter.END, "This is a certified Covid-19 App. All rights reserved 2022")

#TWORZENIE STATUS BAR

    def createStatusBar(self):
        self.statusbar = tk.Label(self.parent, text="Linia statusu",
                                  anchor=tkinter.W)
        self.statusbar.grid(row=2, column=0, columnspan=2,
                            sticky=tkinter.EW)

#EDYCJA STATUS BAR
    def set_status_bar(self, txt):
        self.statusbar["text"] = txt

    def createTaskBar(self):
        self.toolbar_images = []
        self.toolbar = tk.Frame(self.parent)
        for image, command in (
                ("images/country.png", self.createWindowCountry),
                ("images/continent.png", self.createWindowContinent),
                ("images/poland.png", self.createWindowPoland),
                ("images/germany.png", self.createWindowGermany),
                ("images/eu.png", self.createWindowEu),
                ("images/usa.png", self.createWindowUSA)):

            image = os.path.join(os.path.dirname(__file__), image)
            try:
                image = tkinter.PhotoImage(file=image)

                self.toolbar_images.append(image)
                button = tkinter.Button(self.toolbar, image=image,
                                        command=command)
                button.grid(row=0, column=len(self.toolbar_images) - 1)

            except tkinter.TclError as err:
                print(err)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky=tkinter.NSEW)

    def createMenu(self):
        self.menubar = tk.Menu(self.parent)
        self.parent["menu"] = self.menubar
        fileMenu = tk.Menu(self.menubar)
        for label, command in (
                ("Country", self.createWindowCountry),
                ("Continent", self.createWindowContinent),
                ("Country at month", self.createWindowCountryMonth),
                ("Continent at month", self.createWindowContinentMonth),
                ("Country on date", self.createWindowCountryDate),
                ("Continent on date", self.createWindowContinentDate),
                ("Country in period", self.createWindowCountryPeriod),
                ("Continent in period", self.createWindowContinentPeriod),
                (None, None)):
            if label is None:
                fileMenu.add_separator()
            else:
                fileMenu.add_command(label=label, underline=0, command=command)
        self.menubar.add_cascade(label="Options", menu=fileMenu, underline=0)

        fileMenu2 = tk.Menu(self.menubar)
        for label, command, shortcut_text, shortcut in (
                ("About", self.about, "Ctrl+H", "<Control-h>"),
                ("Quit", self.fileQuit, "Ctrl+Q", "<Control-q>"),
                (None, None, None, None)):
            if label is None:
                fileMenu2.add_separator()
            else:
                fileMenu2.add_command(label=label, underline=0,
                                     command=command, accelerator=shortcut_text)
        self.parent.bind(shortcut, command)
        self.menubar.add_cascade(label="Help", menu=fileMenu2, underline=0)


if __name__ == '__main__':
    # makeGui(Controller.Controller("Covid.txt"))
    root = tk.Tk()
    gui = Gui(Controller.Controller("Covid.txt"), master=root)
    gui.mainloop()
