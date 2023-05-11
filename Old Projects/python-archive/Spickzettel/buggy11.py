# Pygame Figuren
import pygame as pg
import random
from math import *
from bplayer import *
from game import *

# Startwerte festlegen
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
xMax, yMax = 800, 600
Winkel = 0
bugMax = 5

# Pygame starten, Spiel-Elemente erzeugen
pg.init()
pg.key.set_repeat(20,20)
pg.display.set_caption("My Game")
Fenster = pg.display.set_mode((xMax, yMax))
Spiel = Game(Green)

# Spielfiguren erzeugen
Figur = []
for Nr in range(0,bugMax) :
  xPos = random.randint(100,xMax-100)
  yPos = random.randint(50,yMax-100)
  Figur.append(Player(xPos, yPos))

# Zufallsrichtung für jede Figur
xStep = []
yStep = []
for Nr in range(0,bugMax) :
  xStep.append(random.randint(0,2))
  if xStep[Nr] == 0 :
    xStep[Nr] = -1
  yStep.append(random.randint(0,2))
  if yStep[Nr] == 0 :
    yStep[Nr] = -1

# Timer starten
Spiel.getTime(True)

# Ereignis-Schleife
running = True
while running :

  # Zeit kontrollieren und anzeigen
  Zeit = Spiel.getTime(False)
  Spiel.showAll(0, Blue)

  # Wenn Zeit vorbei, Ende anzeigen
  if Zeit > bugMax*1500 :
    Spiel.showMessage("Game Over", Red)
    running = False

  for event in pg.event.get() :
    if event.type == pg.QUIT :
      running = False
     
    # Maus abfragen
    if event.type == pg.MOUSEBUTTONDOWN :
      (xPos, yPos) = pg.mouse.get_pos()
      for Nr in range(0,bugMax) :
        if (xPos > Figur[Nr].x) and (xPos < Figur[Nr].x + 100) \
        and (yPos > Figur[Nr].y) and (yPos < Figur[Nr].y + 100) :
          if not Figur[Nr].isKilled :
            Spiel.showAll(50, Blue)
          Figur[Nr].destroy()

  # Grenzen kontrollieren
  for Nr in range(0,bugMax) :
    if (Figur[Nr].x < 0) or (Figur[Nr].x > xMax-110) :
      xStep[Nr] = -xStep[Nr]
    if (Figur[Nr].y < 0) or (Figur[Nr].y > yMax-110) :
      yStep[Nr] = -yStep[Nr]
    
  # Laufrichtung festlegen
  for Nr in range(0,bugMax) :
    Winkel = atan2(-yStep[Nr], xStep[Nr])
    Winkel = degrees(Winkel) - 90
    Figur[Nr].rotate(Winkel)
 
  # Verzögerte Bewegung
  for Nr in range(0,bugMax) :
    if not Figur[Nr].isKilled :
      Figur[Nr].step(xStep[Nr]*2, yStep[Nr]*2)
  pg.time.delay(5)

  # Sprite in Fenster (neu) positionieren
  Fenster.fill(Green)
  Fenster.blit(Spiel.Text, (xMax/4, 10))
  for Nr in range(0,bugMax) :
    Fenster.blit(Figur[Nr].Bild, (Figur[Nr].x, Figur[Nr].y))
  pg.display.update()

# Pygame nach Pause verlassen
pg.time.delay(1500)
pg.quit()

