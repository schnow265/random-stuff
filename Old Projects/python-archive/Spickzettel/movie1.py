# Movie
from tkinter import *

# Fenstermaße und Texte
Breite, Hoehe = 600, 350
Modus = ["Erscheinen", "Bewegen", "Verschwinden"]

# Objekt-Position/Größe
x, y, z = 20, 50, 200

# Event-Funktion
def showImage() :
  global Kreis
  Kreis = Grafik.create_oval(x, y, x+z, y+z, fill="red")
def moveImage() :
  global Kreis
  for pos in range(20,Breite-220,2) :
    Grafik.move(Kreis, 2, 0)
    Grafik.update()
    Grafik.after(10)   
def hideImage() :
  global Kreis
  Grafik.delete(Kreis)

# Hauptprogramm
Fenster = Tk()
Fenster.title("Movie")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
Knopf = []
for Nr in range(0,3) :
  Knopf.append(Button(Fenster, text=Modus[Nr]))
  Knopf[Nr].place(x=80+Nr*150, y=Hoehe-50, width=140, height=30)
Knopf[0].config(command=showImage)
Knopf[1].config(command=moveImage)
Knopf[2].config(command=hideImage)
Fenster.mainloop()

