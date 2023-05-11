# Movie
from tkinter import *

# Maße und Texte
Breite, Hoehe = 600, 400
x, y = 120, 160
Modus = ["Erscheinen", "Bewegen", "Verschwinden"]

# Player-Klasse
class Player :
  Bild = [0]
  def __init__(self, Grafik) :
    for Nr in range(1,9) :
      Name = "Figur0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))
  def showImage(self) :
    self.Figur = Grafik.create_image(x, y, image=self.Bild[1]) 
  def moveImage(self) :
    for pos in range(20,Breite-200,2) :
      Grafik.move(self.Figur, 2, 0)
      Grafik.update()
      Grafik.after(10)   
  def hideImage(self) :
    Grafik.delete(self.Figur)

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
Knopf[0].config(command=Spieler.showImage)
Knopf[1].config(command=Spieler.moveImage)
Knopf[2].config(command=Spieler.hideImage)
Fenster.mainloop()


