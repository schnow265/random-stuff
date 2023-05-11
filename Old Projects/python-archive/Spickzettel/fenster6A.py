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
Anzeige.grid(row=0, column=0, columnspan=2)
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.grid(row=2, column=0, padx=10, pady=10)
Button2.grid(row=2, column=1, padx=10, pady=10)
Fenster.mainloop()

