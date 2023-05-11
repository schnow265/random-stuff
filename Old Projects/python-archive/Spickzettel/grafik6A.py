# Grafik mit Canvas
from tkinter import *
import random

# Farb-Konstanten
Color = ["white", "gray", "red", "green", \
         "blue", "cyan", "yellow", "magenta"]

# Event-Funktion
def buttonClick() :
  for Nr in range(0,5000) :
    x = random.randint(0,Breite)
    y = random.randint(0,Hoehe)
    Farbe = Color[random.randint(0,7)]
    Grafik.create_oval(x,y, x+1, y+1, fill=Farbe)
    
# Hauptprogramm
Fenster = Tk()
Fenster.title("Grafik")
Breite = 500
Hoehe = 330
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe, background="black")
Grafik.pack()
Knopf = Button(Fenster, text="Lass funkeln!", command=buttonClick)
Knopf.place(x=Breite/2-60, y=Hoehe-40, width=120, height=30)
Fenster.mainloop()

