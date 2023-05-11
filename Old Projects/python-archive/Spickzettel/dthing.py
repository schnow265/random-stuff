# Pygame Ding
import pygame as pg
import random

# Ding-Klasse
class Thing(pg.sprite.Sprite) :
  def __init__(self, name, xPos=0, yPos=0) :
    super().__init__()
    self.image = pg.image.load(name)
    self.x, self.y = xPos, yPos
    self.Bild = self.image
    self.Breite = self.Bild.get_width()
    self.Hoehe = self.Bild.get_height()
    self.rect = self.Bild.get_rect()
  def setPosition(self, xPos, yPos, updown) :
    self.x = xPos
    if updown :
      yOyU = random.randint(0,1)
      self.y = yOyU * yPos + self.Hoehe/2
    else :
      self.y = yPos   
  def move(self, xx, yy) :
    self.x += xx
    self.y += yy
  def controlRestart(self, xx, yy) :
    if self.x < 0 :
      yOyU = random.randint(0,1)
      self.x = xx - self.Breite/2
      self.y = yOyU * yy + self.Hoehe/2
      return True
    else :
      return False

