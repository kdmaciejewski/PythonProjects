import tkinter as tk

def gui():

    window = tk.Tk()

    def handle_keypress(event):
        """Print the character associated to the key pressed"""
        print(event.char)

    # Bind keypress event to handle_keypress()
    window.bind("<Key>", handle_keypress)

    def handle_click(event):
        print("The button was clicked!")

    button = tk.Button(text="Click me!")

    button.bind("<Button-2>", handle_click) #klikanie kółkiem
    button.pack()
    window.mainloop()

if __name__ == '__main__':
    gui()
