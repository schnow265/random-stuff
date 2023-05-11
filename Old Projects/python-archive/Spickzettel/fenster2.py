# Fenster mit Buttons
from tkinter import *
Fenster = Tk()
Anzeige = Label(Fenster, text="Hallo, wie geht es?")
Anzeige.pack()
Button1 = Button(Fenster, text="Gut")
Button2 = Button(Fenster, text="Schlecht")
Button1.pack()
Button2.pack()
Fenster.mainloop()

