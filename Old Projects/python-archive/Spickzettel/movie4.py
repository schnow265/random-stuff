# Movie
from tkinter import *
from mplayer import *

# Maße und Texte
Breite, Hoehe = 600, 400
x, y = 120, 160
Modus = ["Erscheinen", "Bewegen", "Verschwinden"]

# Hauptprogramm
Fenster = Tk()
Fenster.title("Movie")
Fenster.config(width=Breite, height=Hoehe)
Grafik = Canvas(Fenster, width=Breite, height=Hoehe)
Grafik.pack()
# Spielfigur
Spieler = Player(Grafik)
# Steuerung
Knopf = []
for Nr in range(0,3) :
  Knopf.append(Button(Fenster, text=Modus[Nr]))
  Knopf[Nr].place(x=80+Nr*150, y=Hoehe-50, width=140, height=30)
Knopf[0].config(command=lambda : Spieler.showImage(x,y,1))
Knopf[1].config(command=lambda : Spieler.moveImage(20,Breite-200))
Knopf[2].config(command=Spieler.hideImage)
Fenster.mainloop()


