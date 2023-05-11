# Fenster
from tkinter import *

# Event-Funktionen
def button1Click() :
  Anzeige.config(text="Das freut mich!")
def button2Click() :
  Anzeige.config(text="Das tut mir leid!")

# Hauptprogramm
Fenster = Tk()
Anzeige = Label(Fenster, text="Hallo! Wie geht es?")
Anzeige.config(font=("Tahoma",12,"normal"))
Anzeige.pack()
Button1 = Button(Fenster, text="Gut", command=button1Click)
Button2 = Button(Fenster, text="Schlecht", command=button2Click)
Button1.config(font=("Tahoma",12,"normal"))
Button2.config(font=("Tahoma",12,"normal"))
Button1.pack(side=LEFT)
Button2.pack(side=RIGHT)
Fenster.mainloop()
