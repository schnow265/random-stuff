# Pygame Figur
import pygame as pg
import random
from math import *
from bplayer import *

# Startwerte festlegen
Green = (0,255,0)
xMax, yMax = 600, 400
Winkel = 0

# Pygame starten, Spielfeld und Spielfigur erzeugen
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Fenster = pg.display.set_mode((xMax, yMax))
Figur = Player(xMax/2-50, yMax/2-50)

# Zufallsrichtung
xStep = random.randint(0,2)
if xStep == 0 :
  xStep = -1
yStep = random.randint(0,2)
if yStep == 0 :
  yStep = -1

# Ereignis-Schleife
running = True
while running :
  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
    # Maus abfragen
    if event.type == pg.MOUSEBUTTONDOWN :
      (xPos, yPos) = pg.mouse.get_pos()
      if (xPos > Figur.x) and (xPos < Figur.x + 100) \
      and (yPos > Figur.y) and (yPos < Figur.y + 100) :
        Figur.destroy()   

  # Grenzen kontrollieren
  if (Figur.x < 0) or (Figur.x > xMax-110) :
    xStep = -xStep
  if (Figur.y < 0) or (Figur.y > yMax-110) :
    yStep = -yStep
    
  # Laufrichtung festlegen
  Winkel = atan2(-yStep, xStep)
  Winkel = degrees(Winkel) - 90
  Figur.rotate(Winkel)
 
  # Verzögerte Bewegung
  if not Figur.isKilled :
    Figur.step(xStep, yStep)
    pg.time.delay(5)

  # Sprite in Fenster (neu) positionieren
  Fenster.fill(Green)
  Fenster.blit(Figur.Bild, (Figur.x, Figur.y))
  pg.display.update()

# Pygame verlassen
pg.quit()

