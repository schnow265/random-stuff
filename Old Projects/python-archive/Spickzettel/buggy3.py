# Pygame Figur
import pygame as pg

# Player-Klasse
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt1.png")
    self.x, self.y = xPos, yPos
    self.Bild = self.image
  def rotate(self, winkel) :
    self.Bild = pg.transform.rotate(self.image, winkel)

# Startwerte festlegen
Green = (0,255,0)
xMax, yMax = 600, 400
Richtung = 0

# Pygame starten, Spielfeld und Spielfigur erzeugen
pg.init()
pg.key.set_repeat(20,20)
Fenster = pg.display.set_mode((xMax, yMax))
Figur = Player(xMax/2-50, yMax/2-50)

# Ereignis-Schleife
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Tasten abfragen
    if event.type == pg.KEYDOWN :
      if event.key == pg.K_LEFT :
        Richtung = 1
        if Figur.x > 0 :
          Figur.x -= 5
      if event.key == pg.K_RIGHT :
        Richtung = 3
        if Figur.x < xMax-100 :
          Figur.x += 5
      if event.key == pg.K_UP :
        Richtung = 0
        if Figur.y > 0 :
          Figur.y -= 5
      if event.key == pg.K_DOWN :
        Richtung = 2
        if Figur.y < yMax-100 :
          Figur.y += 5
      Figur.rotate(Richtung*90)
  
  # Sprite in Fenster (neu) positionieren
  Fenster.fill(Green)
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  pg.display.update()

# Pygame verlassen
pg.quit()
