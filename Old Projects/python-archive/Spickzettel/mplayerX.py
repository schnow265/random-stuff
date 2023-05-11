from tkinter import *

# Player-Klasse
class Player :
  Bild = [0]
  BildNr = 0
  Figur = 0
  
  def __init__(self, grafik) :
    self.Grafik = grafik
    for Nr in range(1,9) :
      Name = "Figur0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.hideImage()
    self.Figur = self.Grafik.create_image(x, y, image=self.Bild[Nr])

  def moveImage(self, von, bis) :
    for pos in range(von, bis, 10) :
      if self.BildNr == 2  :
        self.BildNr = 6
      else :
        self.BildNr = 2
      self.Grafik.itemconfig(self.Figur, image=self.Bild[self.BildNr])     
      self.x, self.y = self.Grafik.coords(self.Figur)    
      if self.x <= bis+100 :
        self.Grafik.move(self.Figur, 10, 0)
        self.Grafik.update()
        self.Grafik.after(100)
    self.Grafik.itemconfig(self.Figur, image=self.Bild[1])

  def turnImage(self) :
    for Nr in range(1, 5) :
      self.Grafik.itemconfig(self.Figur, image=self.Bild[Nr]) 
      self.Grafik.update()
      self.Grafik.after(200)
    self.Grafik.itemconfig(self.Figur, image=self.Bild[1])      
 
  def hideImage(self) :
    self.Grafik.delete(self.Figur)




