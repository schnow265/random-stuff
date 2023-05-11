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
  for Nr in range(0,48) :
    Farbe = Color[random.randint(0,7)]
    Grafik.create_rectangle(Nr*4, Nr*3, Breite-Nr*4, Hoehe-Nr*3, fill=Farbe)
    
# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = Button(Fenster, text="Mal mal!", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe/2-15, width=120, height=30)
Fenster.mainloop()

