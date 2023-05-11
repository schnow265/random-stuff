# Pygame Figur
import pygame as pg

# Player-Klasse
class Player(pg.sprite.Sprite) :
  def __init__(self, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load("Bilder\Insekt2.png")
    self.x, self.y = xPos, yPos
    self.Bild = self.image
    self.isKilled = False
  def rotate(self, winkel) :
    self.Bild = pg.transform.rotate(self.image, winkel)
  def move(self, distanz, xx, yy) :
    self.x += xx
    self.y += yy
    distanz -= 1
    return distanz
  def step(self, xx, yy) :
    self.x += xx
    self.y += yy
  def destroy(self) :
    self.image = pg.image.load("Bilder\Insekt2X.png")
    self.Bild = self.image
    self.isKilled = True

