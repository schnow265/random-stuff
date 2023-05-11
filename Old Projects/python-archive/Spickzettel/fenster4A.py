# Fenster-Ereignisse
from tkinter import *

# Event-Funktionen
def button1Click() :
  Anzeige.config(text="Das freut mich!")
def button2Click() :
  Anzeige.config(text="Das tut mir leid!")

# Hauptprogramm
Fenster = Tk()
Anzeige = Label(Fenster, text="Hallo, wie geht es?")
Anzeige.pack()
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.pack(side="left")
Button2.pack(side="right")
Fenster.mainloop()

