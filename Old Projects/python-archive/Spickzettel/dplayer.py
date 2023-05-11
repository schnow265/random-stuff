# Pygame Figur
import pygame as pg

# Player-Klasse
class Player(pg.sprite.Sprite) :
  image = []
  Dname = ""
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image.append(pg.image.load("Bilder\DoStand.png"))
    self.image.append(pg.image.load("Bilder\DoDuck.png"))
    self.image.append(pg.image.load("Bilder\DoJump.png"))
    self.x, self.y = xPos, yPos
    self.Bild = self.image[0]
    self.Breite = self.Bild.get_width()
    self.Hoehe = self.Bild.get_height()
    self.rect = self.Bild.get_rect()
    self.isHit = False
    self.Status = 0
  def setState(self, Nr) :
    self.Status = Nr
    self.Bild = self.image[Nr]
  def dodge(self, yPos, yMitte) :
    if (yPos < yMitte and self.Status == 1) \
    or (yPos > yMitte and self.Status == 2) :
      return True
    else :
      return False   
  def destroy(self) :
    self.image.append(pg.image.load("Bilder\DoDie.png"))
    self.Bild = self.image[3]
    self.isHit = True
    
  # Übernahme aus der alten Klasse
  def rotate(self, winkel) :
    self.Bild = pg.transform.rotate(self.image[0], winkel)
  def move(self, xx, yy) :
    self.x += xx
    self.y += yy


