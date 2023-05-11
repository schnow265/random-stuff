# Grafik mit Canvas
from tkinter import *
import random

# Fenstermaße
Breite = 500
Hoehe = 330

# Farb-Konstanten
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Event-Funktion
def buttonClick() :
  Farbe = Color[random.randint(0,7)]
  Punkte = [(20,Hoehe-20), (Breite/2,20), (Breite-20,Hoehe-20)]
  Grafik.create_polygon(Punkte, fill=Farbe)
    
# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = Button(Fenster, text="Mal mal!", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe/2+30, width=120, height=30)
Fenster.mainloop()

