# Grafik mit Canvas
from tkinter import *
import random

# Farb-Konstanten
Color = ["gray", "black", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Event-Funktion
def buttonClick() :
  for Nr in range(0,32) :
    Farbe = Color[random.randint(0,7)]
    Schrift = random.randint(10,30)
    Grafik.create_text(random.randint(0,Breite), random.randint(0,Breite), \
    text="Hallo!", fill=Farbe, font=("Arial", Schrift))
    
# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Breite = 500
Hoehe = 330
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = Button(Fenster, text="Schreib mal!", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe/2-15, width=120, height=30)
Fenster.mainloop()

