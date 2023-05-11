# Fenster-Layout
from tkinter import *

# Event-Funktionen
def button1Click() :
  Anzeige.config(text="Das freut mich!")
def button2Click() :
  Anzeige.config(text="Das tut mir leid!")

# Hauptprogramm
Fenster = Tk()
Fenster.config(width=260, height=120)
Anzeige = Label(Fenster, text="Hallo, wie geht es?")
Anzeige.place(x=50, y=20, width=160, height=30)
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.place(x=20, y=70, width=100, height=30)
Button2.place(x=140, y=70, width=100, height=30)
Fenster.mainloop()

