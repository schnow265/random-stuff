# Movie
from tkinter import *

# Fenstermaße und Texte
Breite = 500
Hoehe = 330
Modus = ["Erscheinen", "Bewegen", "Verschwinden"]

# Event-Funktion
def showImage() :
  pass
def moveImage() :
  pass
def hideImage() :
  pass

# Hauptprogramm
Fenster = Tk()
Fenster.title("Movie")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = []
for Nr in range(0,3) :
  Knopf.append(Button(Fenster, text=Modus[Nr]))
  Knopf[Nr].place(x=30+Nr*150, y=Hoehe-50, width=140, height=30)
Knopf[0].config(command=showImage)
Knopf[1].config(command=moveImage)
Knopf[2].config(command=hideImage)
Fenster.mainloop()

