# Fenster-Ereignisse
from tkinter import *

# Event-Funktionen
def button1Click() :
  print("Das freut mich!")
def button2Click() :
  print("Das tut mir leid!")

# Hauptprogramm
Fenster = Tk()
Anzeige = Label(Fenster, text="Hallo, wie geht es?")
Anzeige.pack()
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.pack()
Button2.pack()
Fenster.mainloop()

