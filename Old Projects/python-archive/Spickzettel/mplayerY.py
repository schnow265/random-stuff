from tkinter import *

# Player-Klasse
class Player :
  Bild = [0]
  BildNr = 0
  Figur = 0
  LR = -1
  
  def __init__(self, grafik) :
    self.Grafik = grafik
    for Nr in range(1,9) :
      Name = "Figur0"+str(Nr)+".gif"
      self.Bild.append(PhotoImage(file="Bilder/"+Name))

  def showImage(self, x, y, Nr) :
    self.hideImage()
    self.Figur = self.Grafik.create_image(x, y, image=self.Bild[Nr])

  def moveImage(self, von, bis) :
    self.LR = -self.LR
    for pos in range(von, bis, 10) :
      self.step = 10 * self.LR
      if self.BildNr == 3 - self.LR :
        self.BildNr = 7 - self.LR
      else :
        self.BildNr = 3 - self.LR
      self.Grafik.itemconfig(self.Figur, image=self.Bild[self.BildNr])
      self.x, self.y = self.Grafik.coords(self.Figur)    
      if (self.x >= von+100) and (self.x <= bis+100) :
        self.Grafik.move(self.Figur, self.step, 0)
        self.Grafik.update()
        self.Grafik.after(100)
    self.Grafik.move(self.Figur, -self.step, 0)
    self.Grafik.itemconfig(self.Figur, image=self.Bild[1])

  def turnImage(self) :
    for Nr in range(1, 5) :
      self.Grafik.itemconfig(self.Figur, image=self.Bild[Nr]) 
      self.Grafik.update()
      self.Grafik.after(200)
    self.Grafik.itemconfig(self.Figur, image=self.Bild[1])      
 
  def hideImage(self) :
    self.Grafik.delete(self.Figur)




