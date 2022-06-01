import tkinter
from tkinter import *
import tkinter.messagebox
from datetime import datetime
import configparser
import tkinter as tk
from tkinter.constants import NSEW
import os

class Rapper():
    def __init__(self):
        self.ksywa = "-"

    def name(self):
        tk.messagebox.showinfo("UWAGA", "WAŻNA INFORMACJA")
    def mc(self):
        tk.messagebox.showinfo('Uwaga', f"Witamy, Mc {self.ksywa}")

    def show(self):
        window = tk.Tk()
        window.geometry("500x500")
        window.title("Ulubiony raper twojego ulubionego rapera")

        window.rowconfigure(0, weight=1)
        window.rowconfigure(1, weight=2000)
        frame = tk.Frame()
        greeting = tk.Label(master=frame, text="Hello, Mordoł")
        greeting.grid(column=1, row=0)

        label = tk.Label(master=frame,
            text="Hello, Tkinter",
            foreground="white",  # Set the text color to white
            background="black"  # Set the background color to black
        )

        label.grid(column=1, row=1)
        button = tk.Button(master=frame,text="Click me!",width=25,height=5,bg="orange",fg="yellow",command=self.name)

        button.grid(column=1, row=2)

        l1 = tk.Label(master=frame, text="Mordo, podaj ksywe")
        l1.grid(column=0, row=3)

        e1 = StringVar(value="eel")
        e1 = tk.Entry(master=frame)
        e1.grid(column=1, row=3)

#musi być ta metoda bo inaczej uruhcomi się metoda upgrade zanim pobierzemy wejscie
        def upgrade():
            #print(e1.get())
            self.ksywa = e1.get()
            self.mc()

        button1 = tk.Button(master=frame, text="Wyświetl ksywę", relief=tk.RAISED, borderwidth=10, bg="orange", command=upgrade)
        button1.grid(column=1, row=4)


        l2 = tk.Label(master=frame, text='elo')
        l2.grid(column=1, row=8)        # to nie ma znaczenia tutaj bo zależy od frame
        frame.grid(column=1, row=1)

        statusbar = tk.Label(window, text="Status...", relief=tk.SUNKEN, anchor=tk.W)

        # statusbar.grid(sticky=tk.EW)#, fill=tk.X

        statusbar.grid(row=3, column=0, columnspan=9, sticky=tkinter.EW)
        result = tk.Listbox(window)
        result.grid(row=1, column=2, columnspan=1, rowspan=1, sticky=NSEW)
        result.insert(tkinter.END, 'ebe')
        result.insert(tkinter.END, 'ebe')
        result.insert(tkinter.END, 'ebe')
        result.insert(tkinter.END, 'ebe')

        window.mainloop()


if __name__ == '__main__':
    eldo = Rapper()
    eldo.show()