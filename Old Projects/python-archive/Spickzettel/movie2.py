# Movie
from tkinter import *

# Maße und Texte
Breite, Hoehe = 600, 400
x, y = 120, 160
Modus = ["Erscheinen", "Bewegen", "Verschwinden"]

# Event-Funktion
def showImage() :
  global Figur
  global Bild 
  Bild = PhotoImage(file="Bilder/Figur01.gif")
  Figur = Grafik.create_image(x, y, image=Bild) 
def moveImage() :
  global Figur
  for pos in range(20,Breite-200,2) :
    Grafik.move(Figur, 2, 0)
    Grafik.update()
    Grafik.after(10)   
def hideImage() :
  global Figur
  Grafik.delete(Figur)

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


