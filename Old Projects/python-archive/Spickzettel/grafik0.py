# Grafik mit Canvas
from tkinter import *

# Event-Funktion
def buttonClick() :
  pass

# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=500, height=330)
Knopf = Button(Fenster, text="Mal mal!", command=buttonClick)
Knopf.place(x=190, y=150, width=120, height=30)
Fenster.mainloop()

